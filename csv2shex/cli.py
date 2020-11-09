"""DC Application Profile (DCAP) from CSV to ShEx"""

from dataclasses import asdict
import ruamel.yaml as yaml
import click
from .csvrow import CSVRow
from .csvshape import CSVShape
from .inspect import pprint_csvshapes
from .readwrite import csvreader, get_csvrow_objs_list, get_csvshape_dicts_list
from .settings import CSV_MODEL

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
    csvrow_objs_list = get_csvrow_objs_list(csvreader(csvfile))
    shapes_list = get_csvshape_dicts_list(csvrow_objs_list, expand_prefixes=expand_prefixes)
    pprint_output = pprint_csvshapes(shapes_list)
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


@cli.command()
@click.argument('output_csv', type=click.File('w'), default='-', required=False)
@click.option("--append", is_flag=True)
@click.help_option(help="Show help and exit")
@click.pass_context
def quickcsv(context, output_csv, append):
    """Answer input prompts to create a simple CSV"""

    # csv_model = yaml.safe_load(CSV_MODEL)
    shap = asdict(CSVShape())
    row = asdict(CSVRow())
    shap['statement_csvrows_list'] = row
    for key in list(shap['statement_csvrows_list']):
        if key in list(shap):
            del shap['statement_csvrows_list'][key]

    csv_list = []
    csv_list.append(','.join(row))

    aggregator = []
    for key in list(shap):
        if key != "statement_csvrows_list":
            value = input(f"{key} [{shap[key]}]: ")
            aggregator.append(value)
            for item in aggregator:
                print(item)
            print()

    # a>>> cols = list(row)
    # >>> ','.join(cols)
    # 'shapeID,shapeLabel,shapeClosed,start,propertyID,propertyLabel,manda...
    # >>> [str(value) for value in row.values()]
    # ['None', 'None', 'False', 'False', 'None', 'None', 'False', 'False'...
    # >>> ','.join([str(value) for value in row.values()])
