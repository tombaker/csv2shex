"""Writes YAML configuration file, 'prefixes.yml', to current directory."""

import os
import pytest
from pathlib import Path
from warnings import warn
from csv2shex.config import write_starter_prefixfile, PREFIXFILE_CONTENT, PREFIXFILE_NAME
from csv2shex.exceptions import ConfigWarning


def test_write_starter_prefixfile(tmp_path):
    """Write contents of PREFIXFILE_CONTENT constant to 'prefixes.yml'."""
    os.chdir(tmp_path)
    write_starter_prefixfile()
    assert open(PREFIXFILE_NAME).read() == PREFIXFILE_CONTENT


def test_write_starter_prefixfile_not_if_already_exists(tmp_path):
    os.chdir(tmp_path)
    Path(PREFIXFILE_NAME).write_text(PREFIXFILE_CONTENT)
    assert open(PREFIXFILE_NAME).read() == PREFIXFILE_CONTENT
    with pytest.raises(Warning):
        write_starter_prefixfile()

