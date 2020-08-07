"""Verify that string is valid as URL."""

from csv2shex.utils import is_url

def test_utils_is_url():
    """True if string is valid as URL."""
    assert is_url('http://www.gmd.de')
    assert not is_url('http:///www.gmd.de')
    assert not is_url('file:///www.gmd.de')
    assert not is_url('gmd:')
