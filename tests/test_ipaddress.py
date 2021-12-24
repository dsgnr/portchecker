# First Party
from portchecker.port_checker import is_ip_address
from tests import constants


class TestIsIPAddress:
    def test_is_ip_address_ipv4(self):
        assert is_ip_address(constants.VALID_PRIVATE_IPV4) is True

    def test_is_ip_address_ipv6(self):
        assert is_ip_address(constants.VALID_PRIVATE_IPV6) is True

    def test_is_ip_address_false(self):
        assert is_ip_address(constants.VALID_HOSTNAME) is False
