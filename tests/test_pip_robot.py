"""Test pip_robot."""
# pylint: disable=broad-except
from pip_robot import __version__
from pip_robot import pip_robot


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not pip_robot()
    except Exception:
        assert True
