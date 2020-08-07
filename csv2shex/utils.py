"""Utilities."""

from urllib.parse import urlparse


def is_url(url):
    """True if string is valid as a URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
