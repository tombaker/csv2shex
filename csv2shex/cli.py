"""DC Application Profile (DCAP) from CSV to ShEx"""

import ruamel.yaml as yaml
import click
from .inspect import pprint_csvshapes
from .csvreader import csvreader, get_csvshape_dicts_list
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
    csvshape_dicts_list = get_csvshape_dicts_list(csvrow_dicts_list)
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
    for element_group in ["shape_elements", "cvpair_elements"]:
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
    # shap = asdict(CSVShape())
    # row = asdict(CSVRow())
    # shap['pvdicts_list'] = row
    # for key in list(shap['pvdicts_list']):
    #     if key in list(shap):
    #         del shap['pvdicts_list'][key]

    # csv_list = []
    # csv_list.append(','.join(row))

    # aggregator = []
    # for key in list(shap):
    #     if key != "pvdicts_list":
    #         value = input(f"{key} [{shap[key]}]: ")
    #         aggregator.append(value)
    #         for item in aggregator:
    #             print(item)
    #         print()

    # a>>> cols = list(row)
    # >>> ','.join(cols)
    # 'shapeID,shapeLabel,shapeClosed,start,propertyID,propertyLabel,manda...
    # >>> [str(value) for value in row.values()]
    # ['None', 'None', 'False', 'False', 'None', 'None', 'False', 'False'...
    # >>> ','.join([str(value) for value in row.values()])
