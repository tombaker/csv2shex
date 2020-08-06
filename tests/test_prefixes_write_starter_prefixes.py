"""Writes prefixes.yml to current directory."""

import os
import pytest
#from csv2shex.prefixes import (
#    write_starter_prefixfile,
#    PREFIXFILE_CONTENT,
#    PREFIXFILE_NAME,
#)


@pytest.mark.skip
def test_write_starter_prefixfile(tmp_path):
    """Write contents of constant PREFIXFILE_CONTENT to prefixes.yml."""
    os.chdir(tmp_path)
    write_starter_prefixfile()
    assert open(PREFIXFILE_NAME).read() == PREFIXFILE_CONTENT
