"""Writes YAML configuration file, 'csv2shex.yml', to current directory."""

import os
import pytest
from pathlib import Path
from warnings import warn
from csv2shex.config import write_starter_configfile, CONFIGFILE_CONTENT, CONFIGFILE_NAME
from csv2shex.exceptions import ConfigWarning


def test_write_starter_configfile(tmp_path):
    """Write contents of CONFIGFILE_CONTENT constant to 'csv2shex.yml'."""
    os.chdir(tmp_path)
    write_starter_configfile()
    assert open(CONFIGFILE_NAME).read() == CONFIGFILE_CONTENT


def test_write_starter_configfile_not_if_already_exists(tmp_path):
    os.chdir(tmp_path)
    Path(CONFIGFILE_NAME).write_text(CONFIGFILE_CONTENT)
    assert open(CONFIGFILE_NAME).read() == CONFIGFILE_CONTENT
    with pytest.raises(Warning):
        write_starter_configfile()

