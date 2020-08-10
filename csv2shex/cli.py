"""Generate ShEx schemas from CSV-formatted application profiles."""

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
    """Prepare tabular (CSV) DC Application Profiles for ShEx"""


@cli.command()
@click.option('--model', is_flag=True, default=False)
@click.option('--picklists', is_flag=True, default=False)
@click.option('--prefixes', is_flag=True, default=False)
@click.help_option(help="Show help and exit")
@click.pass_context
def show(context, model, picklists, prefixes):
    """Show DCAP model built-ins for ready reference"""

    if model:
        csv_elements = yaml.safe_load(CSV_ELEMENTS)
        print('DCAP')
        for element_group in ['shape_elements', 'statement_elements']:
            print(f"    {element_group}:")
            for element in csv_elements[element_group]:
                print(f"        {element}")

    if picklists:
        element_picklists = yaml.safe_load(ELEMENT_PICKLISTS)
        print("Built-in value picklists for specific elements:")
        for element in element_picklists:
            print(f"    {element}:")
            for picklist in element_picklists[element]:
                print(f"        {picklist}")

    if prefixes:
        prefix_dict = yaml.safe_load(PREFIXES)['prefixes']
        for prefix in prefix_dict:
            prefix_colon = prefix + ":"
            print(f"{prefix_colon:10} {prefix_dict[prefix]}")


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def yamlparse(context, csvfile):
    """Show CSV file contents as YAML (experimental)"""
    csv2yaml(csvfile)


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def parse(context, csvfile):
    """Show CSV file contents, normalized"""
    statements = list_statements(csvreader(csvfile))
    shapes = list_shapes(statements)
    pprint_output = pprint_shapes(shapes)
    for line in pprint_output.splitlines():
        print(line)
