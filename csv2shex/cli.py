"""Generate ShEx schemas from CSV-formatted application profiles."""

from pathlib import Path
import click
from pprint import pprint
from .prefixes import write_starter_prefixfile, PREFIXFILE_NAME
from .csv2stats import csvreader, list_statements
from .stats2shapes import list_shapes

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
    print(shapes)


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def prefixes(config):
    """Write and display prefixes."""

    write_starter_prefixfile(prefixfile=PREFIXFILE_NAME)
    for line in Path(PREFIXFILE_NAME).open():
        print(line, end="")
