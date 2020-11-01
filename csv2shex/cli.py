"""DC Application Profile (DCAP) from CSV to ShEx"""

import ruamel.yaml as yaml
import click
from .config import CSV_ELEMENTS, ELEMENT_PICKLISTS, PREFIXES
from .csvreader import csvreader
from .csvrows import list_statements
from .csvshapes import pprint_shapes, list_csvshapes
from .mkyaml import csv2yaml

# pylint: disable=unused-argument,no-value-for-parameter
# => unused-argument: Allows placeholders for now.
# => no-value-for-parameter: Okay in cli.py


@click.group()
@click.version_option("0.2.1", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(context):
    """DC Application Profile (DCAP) from CSV to ShEx"""


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.option('--verbose', is_flag=True)
@click.help_option(help="Show help and exit")
@click.pass_context
def examine(context, csvfile, verbose):
    """Show CSV file contents, normalized"""
    statements_list = list_statements(csvreader(csvfile))
    shapes_list = list_csvshapes(statements_list)
    pprint_output = pprint_shapes(shapes_list)
    for line in pprint_output.splitlines():
        print(line)


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
