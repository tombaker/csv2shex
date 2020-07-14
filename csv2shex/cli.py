"""Generate ShEx schemas from CSV-formatted application profiles."""

from pathlib import Path
import click
from .check import check
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
    """Generate ShEx schemas from tabular (CSV) application profiles"""


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def fields(config):
    """Show built-in CSV column headings"""

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
def yamlparse(config, csvfile):
    """Show CSV file contents as YAML"""
    csv2yaml(csvfile)


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def yaml2csv(config, csvfile):
    """Show YAML file as CSV (for round-tripping?)"""
    csv2yaml(csvfile)


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def csvparse(config, csvfile):
    """Show CSV file contents"""
    statements = list_statements(csvreader(csvfile))
    shapes = list_shapes(statements)
    pprint_output = pprint_shapes(shapes)
    for line in pprint_output.splitlines():
        print(line)


@cli.command()
@click.option("--defaults", "Show built-in defaults", is_flag=True)
@click.option("--write", "Write prefixes to ./prefixes.yml", is_flag=True)
@click.help_option(help="Show help and exit")
@click.pass_context
def prefixes(config, defaults, write):
    """Show prefixes, from prefixes.yml if available"""

    if write:
        write_starter_prefixfile(prefixfile=PREFIXFILE_NAME)
        for line in Path(PREFIXFILE_NAME).open():
            print(line, end="")


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def csvcheck(config, csvfile):
    """Check CSV file structure for anomalies"""
    check(csvfile)
