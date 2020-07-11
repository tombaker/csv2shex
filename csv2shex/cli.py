"""Generate ShEx schemas from CSV-formatted application profiles."""

from pathlib import Path
import click
from .config import write_starter_prefixfile, PREFIXFILE_NAME

# pylint: disable=unused-argument
#         During development, unused arguments here.


@click.group()
@click.version_option("0.1", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(config):
    """Generate ShEx schemas from CSV-formatted application profiles."""


@cli.command()
@click.argument("csvfile", type=click.File("r"))
@click.help_option(help="Show help and exit")
@click.pass_context
def parse(config, csvfile):
    """Parse and display CSV file for debugging."""


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def prefixes(config):
    """Write and display prefixes."""

    write_starter_prefixfile(prefixfile=PREFIXFILE_NAME)
    for line in Path(PREFIXFILE_NAME).open():
        print(line, end="")
