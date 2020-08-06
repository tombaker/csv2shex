"""Generate ShEx schemas from CSV-formatted application profiles."""

from pathlib import Path
import click
from .config import CONFIG_DEFAULTS
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
def cli(context):
    """Generate ShEx schemas from tabular (CSV) application profiles"""


@cli.command()
@click.option("--read-from", "Read settings from file", type=click.Path(exists=True))
@click.option("--write-to", "Write settings to file", type=click.Path(exists=False))
@click.help_option(help="Show help and exit")
@click.pass_context
def settings(context, read_from, write_to):
    """Write default settings; read settings from defaults or file."""

    print("Built-in default settings:")
    pprint(yaml.safe_load(CONFIG_DEFAULTS))



@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def yamlparse(context, csvfile):
    """Show CSV file contents as YAML"""
    csv2yaml(csvfile)


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def yaml2csv(context, csvfile):
    """Show YAML file as CSV (for round-tripping?)"""
    csv2yaml(csvfile)


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def csvparse(context, csvfile):
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
def prefixes(context, defaults, write):
    """Show prefixes, from prefixes.yml if available"""

    if write:
        write_starter_prefixfile(prefixfile=PREFIXFILE_NAME)
        for line in Path(PREFIXFILE_NAME).open():
            print(line, end="")


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def csvcheck(context, csvfile):
    """Check CSV file structure for anomalies"""
