"""DC Application Profile (DCAP) from CSV to ShEx"""

import ruamel.yaml as yaml
import click
from .inspect import pprint_csvshapes
from .csvreader import csvreader, _get_csvshape_dicts_list
from .config import CSV_MODEL

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
@click.argument("csvfile_name", type=click.Path(exists=True))
@click.option("--expand-prefixes", is_flag=True)
@click.option("--verbose", is_flag=True)
@click.help_option(help="Show help and exit")
@click.pass_context
def inspect(context, csvfile_name, expand_prefixes, verbose):
    """Inspect CSV file contents, normalized, maybe with expanded prefixes."""
    csvrow_dicts_list = csvreader(csvfile_name)
    csvshape_dicts_list = _get_csvshape_dicts_list(csvrow_dicts_list)
    pprint_output = pprint_csvshapes(csvshape_dicts_list)
    for line in pprint_output:
        print(line)


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def model(context):
    """Show DCAP model built-ins for ready reference"""

    csv_model = yaml.safe_load(CSV_MODEL)
    print("DCAP")
    for element_group in ["shape_elements", "tconstraint_elements"]:
        print(f"    {element_group}:")
        for element in csv_model[element_group]:
            print(f"        {element}")
