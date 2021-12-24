# Third Party
import pytest

# First Party
from portchecker.port_checker import validate
from tests import constants


class TestValidate:
    def test_validate_valid(self):
        assert validate(constants.VALID_HOSTNAME, constants.VALID_PORTS) is True

    def test_validate_invalid_hostname(self):
        with pytest.raises(ValueError, match=constants.NOT_RESOLVE_ERROR):
            validate(constants.INVALID_HOSTNAME, constants.VALID_PORTS)

    def test_validate_invalid_ports(self):
        with pytest.raises(ValueError, match=constants.INVALID_PORT_ERROR):
            validate(constants.VALID_HOSTNAME, constants.INVALID_PORTS_MIX)

    def test_validate_private_ipv4(self):
        with pytest.raises(ValueError, match=constants.NOT_PUBLIC_IP_ERROR):
            validate(constants.VALID_PRIVATE_IPV4, constants.VALID_PORTS)

    def test_validate_public_ipv4(self):
        assert validate(constants.VALID_PUBLIC_IPV4, constants.VALID_PORTS) is True

    def test_validate_public_ipv6(self):
        assert validate(constants.VALID_PUBLIC_IPV6, constants.VALID_PORTS) is True
