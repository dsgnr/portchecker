# Third Party
import pytest

# First Party
from portchecker.port_checker import is_ports_valid
from tests import constants


class TestHostname:
    def test_is_valid_ports(self):
        assert is_ports_valid(constants.VALID_PORTS) is True

    def test_is_invalid_ports(self):
        with pytest.raises(ValueError, match=constants.INVALID_PORT_ERROR):
            is_ports_valid(constants.INVALID_PORTS_MIX)
