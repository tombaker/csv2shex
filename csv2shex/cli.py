"""Generate ShEx schemas from CSV-formatted application profiles."""

import os
from pathlib import Path
import click

# pylint: disable=unused-argument
#         During development, unused arguments here.

@click.group()
@click.version_option("0.1", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(config):
    """Generate ShEx schemas from CSV-formatted application profiles."""


@cli.command()
@click.argument("csvfile", type=click.Path(exists=False), nargs=1, required=False)
@click.help_option(help="Show help and exit")
@click.pass_context
def parse(config, csvfile):
    """Parse and display CSV file."""
    print(f"csvfile: {csvfile}")

