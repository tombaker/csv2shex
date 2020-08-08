"""Core functions of mklists."""

import os
import re
import shutil
from pathlib import Path
from collections import defaultdict
import ruamel.yaml
from .config import CONFIGFILE_NAME, DATADIR_RULEFILE_NAME
from .exceptions import (
    BadFilenameError,
    BadYamlError,
    MklistsError,
    NotUTF8Error,
    DataError,
    RulesError,
)

# pylint: disable=bad-continuation
# Black disagrees.


def apply_rules_to_datalines(rules=None, datalines=None):
    """Returns filename-to-lines dictionary after applying rules to datalines."""
    if not rules:
        raise RulesError("No rules specified.")
    if not datalines:
        raise DataError("No data specified.")

    f2lines_dict = defaultdict(list)
    is_first_rule = True
    for rule in rules:
        pattern = rule.source_matchpattern
        matchfield = rule.source_matchfield
        if is_first_rule:
            f2lines_dict[rule.source] = datalines
            is_first_rule = False

        for line in f2lines_dict[rule.source][:]:
            if _line_matches_pattern(pattern, matchfield, line):
                f2lines_dict[rule.target].append(line)
                f2lines_dict[rule.source].remove(line)

        target_lines = f2lines_dict[rule.target]
        sortorder = rule.target_sortorder
        f2lines_dict[rule.target] = _dsusort_lines(target_lines, sortorder)

    return dict(f2lines_dict)


def _dsusort_lines(lines=None, sortorder=None):
    """Returns list of datalines sorted by awkfield-numbered sort-order."""
    if not lines:
        raise DataError("No lines to sort.")
    if sortorder == 0:
        return sorted(lines)
    if not sortorder:
        return lines
    if sortorder > 0:
        zeroeth_sortorder = sortorder - 1
        decorated_lines = []
        for line in lines:
            if sortorder > len(line.split()):
                decorated_line = (line, "")
            else:
                decorated_line = (line, line.split()[zeroeth_sortorder])
            decorated_lines.append(decorated_line)

        decorated_lines.sort(key=lambda item: item[1])
        return [line for (line, __) in decorated_lines]
    return lines


def _line_matches_pattern(pattern=None, field_int=None, line=None):
    """Line matches if given field matches given pattern."""
    if field_int > len(line.split()):
        return False
    if field_int == 0:
        if re.search(pattern, line):
            return True
    if field_int > 0:
        field_str = line.split()[field_int - 1]
        if re.search(pattern, field_str):
            return True
    return False


def find_data_subdir_paths(
    datadir=None, configfile=CONFIGFILE_NAME, rulefile=DATADIR_RULEFILE_NAME
):
    """Return list of data directories below given directory."""
    if not datadir:
        datadir = Path.cwd()
    datadir_paths = []
    for dirpath, dirs, files in os.walk(datadir):
        dirs[:] = [d for d in dirs if not d[0] == "."]
        if rulefile in files:
            if configfile not in files:
                datadir_paths.append(Path(dirpath))
    return datadir_paths


def get_configdict(rootdir_path=None, configfile_name=CONFIGFILE_NAME):
    """Returns configuration dictionary from YAML config file (or exits with errors."""
    if not rootdir_path:
        rootdir_path = _find_rootdir_path()
    configfile = Path(rootdir_path) / configfile_name
    try:
        configfile_contents = Path(configfile).read_text()
    except FileNotFoundError:
        raise MklistsError(f"Config file {repr(configfile)} not found.")
    try:
        return ruamel.yaml.safe_load(configfile_contents)
    except ruamel.yaml.YAMLError:
        raise BadYamlError(f"Badly formatted YAML content.")


def get_datalines(datadir=None, bad_filename_patterns=None):
    """Returns lines from files in current directory (or exits with errors)."""
    if not datadir:
        datadir = Path.cwd()
    visiblefiles_list = _ls_visiblefile_paths(datadir)
    all_datalines = []
    for datafile in visiblefiles_list:
        try:
            datafile_lines = open(datafile).readlines()
        except UnicodeDecodeError:
            raise NotUTF8Error(f"{repr(datafile)} is not UTF8-encoded.")
        if bad_filename_patterns:
            for badpat in bad_filename_patterns:
                if re.search(badpat, datafile):
                    raise BadFilenameError(f"{repr(datafile)} matches {repr(badpat)}.")
        for line in datafile_lines:
            if not line.rstrip():
                raise DataError(f"{repr(datafile)} must have no blank lines.")
        all_datalines.extend(datafile_lines)
    if not all_datalines:
        raise DataError("No data to process!")
    return all_datalines


def _find_rootdir_path(datadir=None, configfile=CONFIGFILE_NAME):
    """Return root pathname of mklists repo wherever executed in repo."""
    if not datadir:
        datadir = Path.cwd()
    parents = list(Path(datadir).parents)
    parents.insert(0, Path.cwd())
    for directory in parents:
        if configfile in [item.name for item in directory.glob("*")]:
            return Path(directory)
    raise MklistsError(f"{repr(configfile)} not found - not a repo.")


def _ls_visiblefile_paths(datadir=None):
    """Return list of pathnames of visible files (if all filenames are valid)."""
    if not datadir:
        datadir = Path.cwd()
    visiblefile_paths = []
    all_fns = [str(p) for p in Path(datadir).glob("*") if os.path.isfile(p)]
    all_fns_minus_dotfiles = [f for f in all_fns if not re.match(r"\.", Path(f).name)]
    if all_fns_minus_dotfiles:
        for fn in all_fns_minus_dotfiles:
            visiblefile_paths.append(fn)
    return sorted(visiblefile_paths)


def move_specified_datafiles_elsewhere(files2dirs_dict=None, rootdir_path=None):
    """Moves data files to specified destination directories."""
    for key in files2dirs_dict:
        destination_dir = Path(rootdir_path) / files2dirs_dict[key]
        if os.path.exists(key):
            if os.path.exists(destination_dir):
                shutil.move(key, destination_dir)


def write_new_datafiles(filenames2lines_dict=None):
    """Writes contents of file2lines dictionary to disk files."""
    for (key, value) in filenames2lines_dict.items():
        if value:
            with open(key, "w", encoding="utf-8") as fout:
                fout.writelines(value)
