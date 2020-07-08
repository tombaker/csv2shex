"""@@@Docstring"""

import os
import pytest
from csv2shex.cli import cli
from click.testing import CliRunner


def test_cli():
    """@@@Docstring"""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert result.output == "Hello, world!\n"
