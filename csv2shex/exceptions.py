"""Exception classes for mklists."""


class Csv2shexError(SystemExit):
    """Exceptions related to Mklists generally."""


class ConfigError(Csv2shexError):
    """Exceptions related to configuration."""


class ConfigWarning(Warning):
    """Warning regarding configuration (does not stop execution)."""


class StatementError(Csv2shexError):
    """Exceptions related to a single Statement."""


class CsvError(Csv2shexError):
    """Exceptions related to an entire CSV-derived object."""


class BadRegexError(SystemExit):
    """String does not compile as regular expression."""


class NotUTF8Error(SystemExit):
    """File is not UTF8-encoded."""

