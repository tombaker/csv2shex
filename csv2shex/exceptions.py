"""Exception classes for mklists."""


class Csv2shexError(SystemExit):
    """Exceptions related to Mklists generally."""


class ConfigError(Csv2shexError):
    """Exceptions related to configuration."""


class CSVRowError(Csv2shexError):
    """Exceptions related to a single CSVRow."""


class UristemValueError(Csv2shexError):
    """Exceptions related to UriStem value."""


class CsvError(Csv2shexError):
    """Exceptions related to an entire CSV-derived object."""


class BadRegexError(SystemExit):
    """String does not compile as regular expression."""


class BadYamlError(SystemExit):
    """YAML does not parse."""


class NotUTF8Error(SystemExit):
    """File is not UTF8-encoded."""


class ConfigWarning(Warning):
    """Warning regarding configuration (does not stop execution)."""
