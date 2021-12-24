# Third Party
import pytest

# First Party
from portchecker.port_checker import check_connect
from tests import constants


class TestConnect:
    def test_connectectable_ipv4(self):
        addr, connectable = check_connect(
            constants.SOCKET_ADDR_IPV4_CONNECTABLE, constants.SOCKET_TIMEOUT
        )
        assert addr[0] == constants.VALID_PUBLIC_IPV4
        assert addr[1] == constants.CONNECTABLE_PORT
        assert connectable is True

    def test_nonconnectectable_ipv4(self):
        addr, connectable = check_connect(
            constants.SOCKET_ADDR_IPV4_NOT_CONNECTABLE, constants.SOCKET_TIMEOUT
        )
        assert addr[0] == constants.VALID_PUBLIC_IPV4
        assert addr[1] == constants.NOT_CONNECTABLE_PORT
        assert connectable is False

    @pytest.mark.xfail
    def test_connectectable_ipv6(self):
        addr, connectable = check_connect(
            constants.SOCKET_ADDR_IPV6_CONNECTABLE, constants.SOCKET_TIMEOUT
        )
        assert addr[0] == constants.VALID_PUBLIC_IPV6
        assert addr[1] == constants.CONNECTABLE_PORT
        assert connectable is True

    @pytest.mark.xfail
    def test_nonconnectectable_ipv6(self):
        addr, connectable = check_connect(
            constants.SOCKET_ADDR_IPV6_NOT_CONNECTABLE, constants.SOCKET_TIMEOUT
        )
        assert addr[0] == constants.VALID_PUBLIC_IPV6
        assert addr[1] == constants.NOT_CONNECTABLE_PORT
        assert connectable is False
