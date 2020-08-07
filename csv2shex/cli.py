"""Generate ShEx schemas from CSV-formatted application profiles."""

# from pathlib import Path
from pprint import pprint
import ruamel.yaml as yaml
import click
from .config import CSV_ELEMENTS, ELEMENT_PICKLISTS, PREFIXES
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
@click.help_option(help="Show help and exit")
@click.pass_context
def elements(context):
    """Show elements of model (CSV column headers)."""

    elements = yaml.safe_load(CSV_ELEMENTS)
    print('DCAP')
    for element_group in ['shape_elements', 'statement_elements']:
        print(f"    {element_group}:")
        for element in elements[element_group]:
            print(f"        {element}")


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def picklists(context):
    """Show built-in picklists for specific elements."""

    picklists = yaml.safe_load(ELEMENT_PICKLISTS)
    print("Built-in value picklists:")
    for element in picklists:
        print(f"    {element}:")
        for picklist in picklists[element]:
            print(f"        {picklist}")


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def prefixes(context):
    """Show built-in prefix bindings."""

    prefix_dict = yaml.safe_load(PREFIXES)['prefixes']
    for prefix in prefix_dict:
        prefix_colon = prefix + ":"
        print(f"{prefix_colon:10} {prefix_dict[prefix]}")


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
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def csvcheck(context, csvfile):
    """Check CSV file structure for anomalies"""
