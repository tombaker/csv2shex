"""DC Application Profile (DCAP) from CSV to ShEx"""

import ruamel.yaml as yaml
import click
from .csvreader import csvreader
from .csvrows import get_csvrowobjs_list
from .csvshapes import pprint_schema, get_csvshapes_dict
from .defaults import CSV_MODEL

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
@click.option("--expand-prefixes", is_flag=True)
@click.option("--verbose", is_flag=True)
@click.help_option(help="Show help and exit")
@click.pass_context
def inspect(context, csvfile, expand_prefixes, verbose):
    """Inspect CSV file contents, normalized, maybe with expanded prefixes."""
    csvrowobjs_list = get_csvrowobjs_list(csvreader(csvfile))
    shapes_list = get_csvshapes_dict(csvrowobjs_list, expand_prefixes=expand_prefixes)
    pprint_output = pprint_schema(shapes_list)
    for line in pprint_output:
        print(line)


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def model(context):
    """Show DCAP model built-ins for ready reference"""

    csv_model = yaml.safe_load(CSV_MODEL)
    print("DCAP")
    for element_group in ["shape_elements", "statement_elements"]:
        print(f"    {element_group}:")
        for element in csv_model[element_group]:
            print(f"        {element}")
