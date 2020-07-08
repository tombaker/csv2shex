"""Generate ShEx schemas from CSV-formatted application profiles."""

import os
from pathlib import Path
import click

# pylint: disable=unused-argument
#         During development, unused arguments here.

@click.group()
@click.version_option("0.1", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(config):
    """Generate ShEx schemas from CSV-formatted application profiles."""
    # ctx.obj = get_configdict()
    #     verbose = ctx.obj["verbose"]
    #     backups = ctx.obj["backup_depth"]
    #     will_linkify = ctx.obj["linkify"]
    #     fname_patterns = ctx.obj["invalid_filename_patterns"]
    #     files2dirs = ctx.obj["files2dirs_dict"]
    #     pathstems = ctx.obj["pathstem_list"]


@cli.command()
@click.argument("directory", type=click.Path(exists=False), nargs=1, required=False)
@click.option("--bare", is_flag=True, help="Write minimal rule file.")
@click.help_option(help="Show help and exit")
@click.pass_context
def init(config, directory, bare):
    """Initialize list repo."""
    print(f"config: {config}")
    print(f"directory: {directory}")
    print(f"bare: {bare}")

@cli.command()
@click.option("--dryrun", is_flag=True, help="Run verbosely in read-only mode")
@click.option("--here-only", is_flag=True, help="Sync cwd only (the default)")
@click.option("--here-subdirs", is_flag=True, help="Sync cwd and directories below")
@click.option("--root-subdirs", is_flag=True, help="Sync all data directories in repo")
@click.help_option(help="Show help and exit")
@click.pass_context
def sync(config, dryrun, here_subdirs, here_only, root_subdirs):
    """Rebuild lists, by default in current directory and subdirs"""

