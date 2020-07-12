"""Generate ShEx schemas from CSV-formatted application profiles."""

from pathlib import Path
from pprint import pprint
from dataclasses import asdict
import click
from .prefixes import write_starter_prefixfile, PREFIXFILE_NAME
from .mkstatements import csvreader, list_statements
from .mkshapes import pprint_shapes, list_shapes

# pylint: disable=unused-argument
#         During development, unused arguments here.


@click.group()
@click.version_option("0.1", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(config):
    """Generate ShEx schemas from CSV-formatted application profiles."""


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def parse(config, csvfile):
    """Parse and display CSV file for debugging."""

    statements = list_statements(csvreader(csvfile))
    shapes = list_shapes(statements)
    pprint_output = pprint_shapes(shapes)
    for line in pprint_output.splitlines():
        print(line)


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def prefixes(config):
    """Write and display prefixes."""

    write_starter_prefixfile(prefixfile=PREFIXFILE_NAME)
    for line in Path(PREFIXFILE_NAME).open():
        print(line, end="")
