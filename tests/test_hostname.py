# Third Party
import pytest

# First Party
from portchecker.port_checker import is_valid_hostname
from tests import constants


class TestHostname:
    def test_is_valid_hostname(self):
        assert is_valid_hostname(constants.VALID_HOSTNAME) is True

    def test_is_invalid_hostname(self):
        with pytest.raises(ValueError, match=constants.NOT_RESOLVE_ERROR):
            is_valid_hostname(constants.INVALID_HOSTNAME)
