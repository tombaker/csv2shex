"""Generate ShEx schemas from CSV-formatted application profiles."""

from pathlib import Path
from pprint import pprint
from dataclasses import asdict
import click
from .prefixes import write_starter_prefixfile, PREFIXFILE_NAME
from .mkstatements import csvreader, list_statements
from .mkshapes import list_shapes

# pylint: disable=unused-argument
#         During development, unused arguments here.


@click.group()
@click.version_option("0.1", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(config):
    """Generate ShEx schemas from CSV-formatted application profiles."""


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.help_option(help="Show help and exit")
@click.pass_context
def parse(config, csvfile):
    """Parse and display CSV file for debugging."""

    statements = list_statements(csvreader(csvfile))
    shapes = list_shapes(statements)
    for item in shapes:
        item = asdict(item)
        print(f"Shape")
        print(f"    start:    {item['start']}")
        print(f"    shape_id: {item['shape_id']}")
        if item['shape_label']:
            print(f"    shape_label: {item['shape_label']}")
        for row in item['shape_statements']:
            print(f"    Statement")
            print(f"        prop_id:          {row['prop_id']}")
            if row['prop_label']:
                print(f"        prop_label:       {row['prop_label']}")
            if row['mand']:
                print(f"        mand:             {row['mand']}")
            if row['repeat']:
                print(f"        repeat:           {row['repeat']}")
            if row['value_type']:
                print(f"        value_type:       {row['value_type']}")
            if row['value_datatype']:
                print(f"        value_datatype:   {row['value_datatype']}")
            if row['constraint_value']:
                print(f"        constraint_value: {row['constraint_value']}")
            if row['constraint_type']:
                print(f"        constraint_type:  {row['constraint_type']}")
            if row['shape_ref']:
                print(f"        shape_ref:        {row['shape_ref']}")
            if row['annot']:
                print(f"        annot:            {row['annot']}")


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def prefixes(config):
    """Write and display prefixes."""

    write_starter_prefixfile(prefixfile=PREFIXFILE_NAME)
    for line in Path(PREFIXFILE_NAME).open():
        print(line, end="")
