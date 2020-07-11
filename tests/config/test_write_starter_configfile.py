"""Writes YAML configuration file, 'prefixes.yml', to current directory."""

import os
from csv2shex.config import write_starter_prefixfile, PREFIXFILE_CONTENT, PREFIXFILE_NAME


def test_write_starter_prefixfile(tmp_path):
    """Write contents of PREFIXFILE_CONTENT constant to 'prefixes.yml'."""
    os.chdir(tmp_path)
    write_starter_prefixfile()
    assert open(PREFIXFILE_NAME).read() == PREFIXFILE_CONTENT
