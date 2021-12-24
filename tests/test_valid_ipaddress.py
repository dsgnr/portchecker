# Third Party
import pytest

# First Party
from portchecker.port_checker import is_address_valid
from tests import constants


class TestValidIPAddress:
    def test_valid_public_ipv4(self):
        assert is_address_valid(constants.VALID_PUBLIC_IPV4) is True

    def test_valid_public_ipv6(self):
        assert is_address_valid(constants.VALID_PUBLIC_IPV6) is True

    def test_invalid_ipv4_failure(self):
        with pytest.raises(ValueError, match=constants.NOT_VALID_IP_ERROR):
            is_address_valid(constants.INVALID_PUBLIC_IPV4)

    def test_invalid_ipv6_failure(self):
        with pytest.raises(ValueError, match=constants.NOT_VALID_IP_ERROR):
            is_address_valid(constants.INVALID_PUBLIC_IPV6)

    def test_private_ipv4_failure(self):
        with pytest.raises(ValueError, match=constants.NOT_PUBLIC_IP_ERROR):
            is_address_valid(constants.VALID_PRIVATE_IPV4, allow_private=False)

    def test_private_ipv6_failure(self):
        with pytest.raises(ValueError, match=constants.NOT_PUBLIC_IP_ERROR):
            is_address_valid(constants.VALID_PRIVATE_IPV6, allow_private=False)
