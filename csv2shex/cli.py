"""Generate ShEx schemas from CSV-formatted application profiles."""

from pathlib import Path
import click
from .constants import PREFIXFILE_NAME, SHAPE_KEYS, STATEMENT_KEYS
from .prefixes import write_starter_prefixfile
from .mkstatements import csvreader, list_statements
from .mkshapes import pprint_shapes, list_shapes
from .mkyaml import csv2yaml

# pylint: disable=unused-argument,no-value-for-parameter
# => unused-argument: Allows placeholders for now.
# => no-value-for-parameter: Okay in cli.py


@click.group()
@click.version_option("0.1", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(config):
    """Generate ShEx schemas from CSV-formatted application profiles."""


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def fields(config):
    """Display CSV column headings."""

    print(f"Shape")
    for key in SHAPE_KEYS:
        print(f"    {key}")

    print("")
    print(f"    Statement")
    for key in STATEMENT_KEYS:
        print(f"        {key}")


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def csvcheck(config, csvfile):
    """Parse CSV file and print ."""
    csv2yaml(csvfile)


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def csv_to_yaml(config, csvfile):
    """Parse CSV file and print contents as YAML."""
    csv2yaml(csvfile)


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def csvparse(config, csvfile):
    """Parse CSV file and print content."""
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
