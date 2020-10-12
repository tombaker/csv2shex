"""Normalize a CSV header to snake case."""

from csv2shex.csvreader import _snakify


def test_snakify_dashes_to_underscores():
    """Replaces dashes with underscores - and lowercases."""
    assert _snakify("abc-def-ghi") == "abc_def_ghi"


def test_snakify_spaces_to_underscores():
    """Replaces spaces with underscores - and lowercases."""
    assert _snakify("abc def ghi") == "abc_def_ghi"


def test_snakify_camelcase_to_underscores():
    """Replaces spaces with underscores - and lowercases."""
    assert _snakify("abcDefGhi") == "abc_def_ghi"


def test_snakify_uppercase_to_lowercase():
    """Replaces uppercase with lowercase."""
    assert _snakify("Abc_def_ghi") == "abc_def_ghi"
