import os
import click
from pathlib import Path
from spy.constants import EXCLUDE, NAMES2DIRS
from spy.search import get_files_to_search, search

@click.command()
@click.option("--abc", is_flag=True, default=False)
@click.option("--abcd", is_flag=True, default=False)
@click.option("--agenda", is_flag=True, default=False)
@click.option("--agendab", is_flag=True, default=False)
@click.option("--agendabc", is_flag=True, default=False)
@click.option("--ai", is_flag=True, default=False)
@click.option("--aii", is_flag=True, default=False)
@click.option("--handles", is_flag=True, default=False)
@click.option("--logs", is_flag=True, default=False)
@click.option("--mems", is_flag=True, default=False)
@click.option("--mes", is_flag=True, default=False)
@click.option("--phone", is_flag=True, default=False)
@click.option("--x", is_flag=True, default=False)
@click.option("--xlog", is_flag=True, default=False)
@click.option("--y", is_flag=True, default=False)
@click.option("--ylog", is_flag=True, default=False)
@click.option("--z", is_flag=True, default=False)
@click.option("--acct", is_flag=True, default=False)
@click.option("--cicero", is_flag=True, default=False)
@click.option("--orange", is_flag=True, default=False)
@click.option("--here", is_flag=True, default=False)
@click.argument("terms", nargs=-1)
def cli(
    abc,
    abcd,
    agenda,
    agendab,
    agendabc,
    ai,
    aii,
    handles,
    logs,
    mems,
    mes,
    phone,
    x,
    xlog,
    y,
    ylog,
    z,
    acct,
    cicero,
    orange,
    here,
    terms,
):
    """Docstring@@"""
    cli_args = locals()
    if not terms:
        here = True

    dirs_to_search = []
    for key in NAMES2DIRS.keys():
        if cli_args[key]:
            dirs_to_search.append(NAMES2DIRS[key])

    files_to_search = get_files_to_search(dirs_to_search)
    search_terms = terms

    result = search(files_to_search, search_terms)
    for line in result:
        print(line, end='')

