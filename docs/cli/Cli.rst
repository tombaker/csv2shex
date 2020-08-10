Command-line tool
-----------------

To get basic help, run the command with no arguments or with the '--help' option::

    $ csv2shex
    $ csv2shex --help

The subcommand 'parse' reads and displays the contents of a given CSV file (here: 'example.csv')::

    $ csv2shex parse example.csv

The subcommend 'show' displays program built-ins for the DCAP model, element-specific value picklists, and namespace prefix bindings, respectively::

    $ csv2shex show --model
    $ csv2shex show --picklists
    $ csv2shex show --prefixes

The subcommand 'yamlparse' has been implemented experimentally as a proof-of-concept::

    $ csv2shex yamlparse example.csv
