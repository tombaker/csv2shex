Command-line utility
--------------------

As of 2020-08-09, the command-line interface is:

    Usage: csv2shex [OPTIONS] COMMAND [ARGS]...

      Generate ShEx schemas from tabular (CSV) DC Application Profiles

    Options:
      --version  Show version and exit
      --help     Show help and exit

    Commands:
      csvparse   Show CSV file contents, normalized
      elements   Show elements of the DCAP model (CSV column headers)
      picklists  Show built-in picklists for specific elements
      prefixes   Show built-in prefix bindings
      yaml2csv   Show YAML file as CSV (for round-tripping?)
      yamlparse  Show CSV file contents as YAML

The main subcommand used to read and display the contents of a CSV file is:

    $ csv2shex csvparse example.csv

Several other subcommands provide quick access to the elements of the model, picklists for specific elements, and built-in prefix bindings.

A 'yamlparse' subcommand has been implemented as proof-of-concept. A 'yaml2csv' subcommand is still just aspirational.
