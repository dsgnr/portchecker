#!/usr/bin/env python3
"""
This is a small Python script which can be called by AWS Lambda to
verify the connectivity state of DNS hostnames, IPv4 or IPv6 addresses.

Maintainer: Dan Hand (info@portchecker.io)
GitHub: https://github.com/dsgnr/api.portchecker.io
"""

# Standard Library
import argparse
import concurrent.futures
import json
import sys
from ipaddress import ip_address
from socket import (
    AF_INET,
    AF_INET6,
    IPPROTO_TCP,
    SOCK_STREAM,
    gaierror,
    getaddrinfo,
    gethostbyname,
    socket,
    timeout as socket_timeout,
)


def is_ip_address(address: str) -> bool:
    """
    Determines whether the supplied address is an IP address.

    :param address: The IPv4, IPv6 or hostname we would like to validate
    :type: address: str
    :return: bool

    :raises ValueError: If the provided address is not a valid IP address (eg, it's a hostname)
    """
    try:
        return bool(ip_address(address))
    except ValueError:
        return False


def is_address_valid(address: str) -> bool:
    """
    Determines whether the supplied IP address is public.

    :param address: The IPv4, IPv6 or hostname we would like to validate
    :type: address: str
    :return: bool

    :raises ValueError: If the provided address is not a valid public IP address (eg, not RFC1918)
    """
    address_obj = ip_address(address)
    if address_obj.is_private:
        raise ValueError(
            f"IPv{address_obj.version} address '{address}' does not appear to be public"
        )
    return True


def is_valid_hostname(hostname: str) -> bool:
    """
    Determines whether the supplied hostname can be resolved.

    :param hostname: The hostname we would like to validate
    :type: hostname: str
    :return: bool

    :raises ValueError: If the provided hostname can not be resolved
    """
    try:
        gethostbyname(hostname)
        return True
    except gaierror:
        raise ValueError(f"Hostname '{hostname}' does not appear to resolve")


def is_ports_valid(ports: list) -> bool:
    """
    Determines whether the supplied list of ports is within the valid range.

    :param ports: A list of ports to check
    :type: hostname: list
    :return: bool

    :raises ValueError: If any number of the provided ports are outside the valid range
    """
    invalid = []
    for port in ports:
        if 1 <= int(port) <= 65535:
            continue
        invalid.append(str(port))
    if invalid:
        raise ValueError(f"Port(s) '{', '.join(invalid)}' is not in a valid range of (1-65535)")
    return True


def check_connect(address: tuple, timeout: int = 2) -> tuple:
    """
    Attempts to make a socket connection to the address tuple provided.
    Example tuple: `('142.250.178.14', 443)`

    :param address: A tuple containing the IP address and port generated by `socket.getaddrinfo`
    :type: address: tuple
    :return: tuple
    """
    connectable = False
    try:
        inet = AF_INET if ip_address(address[0]).version == 4 else AF_INET6
        sock = socket(inet, SOCK_STREAM, 0)
        sock.settimeout(timeout)
        sock.connect(address)
        sock.close()
        connectable = True
    except socket_timeout:
        pass
    return address, connectable


def validate(host: str, ports: list) -> bool:
    """
    Validates the provided host and port list is a valid public IP address or a resolvable hostname

    :param host: An IPv4, IPv6 or hostname to validate
    :type host: str
    :param ports: A list of TCP ports to validate
    :type: ports: list
    :return: bool

    :raises ValueError: If the provided host is not a resolvable DNS hostname
    :raises ValueError: If the provided host is not a valid public IPv4 or IPv6 address
    :raises ValueError: If any number of the provided ports is ouside the valid range
    """
    is_ip = is_ip_address(host)
    is_ports_valid(ports)
    if is_ip:
        is_address_valid(host)
    else:
        is_valid_hostname(host)
    return True


def do_portcheck(address, ports):
    """
    The main function called by Lambda
    """
    validate(address, ports)
    output = {}
    found_addresses = []
    for port in ports:
        for sockaddr in getaddrinfo(address, port, proto=IPPROTO_TCP):
            found_addresses.append(sockaddr[-1])

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {executor.submit(check_connect, url): url for url in found_addresses}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            address, connectable = future.result()
            output.setdefault(address[0], {})
            output[address[0]].setdefault("type", f"ipv{ip_address(address[0]).version}")
            output[address[0]].setdefault("results", [])
            output[address[0]]["results"].append({"port": address[1], "connectable": connectable})
    return output


def main() -> dict:
    """
    The entrypoint of the script.
    """
    parser = argparse.ArgumentParser(
        description="Query the port status of a given hostname or IP address"
    )
    parser.add_argument(
        '--host', type=str, required=True, help="The hostname or IP address to query"
    )
    parser.add_argument(
        '--ports',
        type=int,
        nargs='*',
        required=True,
        help="A space separated list of ports to query",
    )
    args = parser.parse_args()
    supplied_address = args.host
    supplied_ports = args.ports
    print(json.dumps(do_portcheck(supplied_address, supplied_ports), indent=4))


if __name__ == "__main__":
    sys.exit(main())
