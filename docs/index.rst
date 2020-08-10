csv2shex
========

Csv2shex is a command-line utility for reading, interpreting, and verifying CSV files formatted according to the DC Application Profile (DCAP) model. The utility interprets and normalizes the contents of a CSV files and prints the results to standard outpus as an aid for debugging. The utility also experimentally converts the CSV contents into a YAML representation. The ultimate goal of this project is to convert instances of DCAP in CSV into ShEx schemas usable for data validation.

This project has been undertaken in parallel to, and in support of, a working group of the Dublin Core Metadata Initiative which is creating the DCAP model (@@@add links).

The motivation for this project is to make the ShEx data validation language, with its own syntax, accessible to users who are "spreadsheet-enabled", ie who are comfortable with tabular formats. The tabular format, it is hoped, will serve as an "on-ramp" to the more expressive ShEx language by providing an easy way to generate, and to understand, the first draft of a schema in ShEx. 

The code in this project tries to anticipate messy or incomplete CSV inputs and to fill gaps and normalize inconsistencies. For example, the code allows users to enter URIs either as full URIs (with or without enclosing angle brackets) or as abbreviated URIs written with namespace prefixes (e.g., 'dcterms:creator'), or to enter the datatypes of literal values without using an extra column to specify that the value is a Literal (since this can be inferred).

As of August 2020, work both in this project and in the context of the DCMI working group has focused on defining the DCAP model and its elements (concretely: the fixed set of CSV column headers). As the nature and definition of these elements is still somewhat in flux, the descriptions provided in this documentation should be considered provisional.

Our hope is that a simple, well-defined model, expressible in CSV and convertible into YAML, will provide a solid basis for generating validation schemas in ShEx.

It is also our hope that modules and Python classes on which this command-line utility can be adapted for use in other environments. This documentation explains how CSV files are interpreted and normalized. For an up-to-the-minute look at how the modules and classes work, the reader is invited to inspect (and execute) the pytest unit tests, which have been formulated for ease of comprehension.

Potential directions for the further development of this project include:

- Resolution of prefixed URIs to full URIs on the basis of a table of namespace prefixes.

- The ability to tweak built-in defaults in local configuration files.

- The ability to read namespace prefixes from sources on the Web or from local configuration files.

- The ability to round-trip from a messy, first-draft CSV expression of a DCAP, via a normalized expression in Python, then (potentially) back to a normalized expression in CSV.

- The ability to capture the Python expression of a DCAP as a reusable (and editable) YAML document.

- The ability to write the Python expression of a DCAP to an Excel spreadsheet, potentially with tabs for namespace prefixes and controlled sets of values (such as the four main value types URI, Literal, Nonliteral, and BNode) linked to specific columns of the main sheet for use as dropdown menus.

To complete the conversion of CSV into ShEx, the next big task of this work will be to work out how the elements of the DCAP model interface with existing Python modules for generating ShEx schemas (@@@links).

.. toctree::
   :maxdepth: 3

   install/Install
   cli/Cli
   basics/Basics
   normalizations/Normalizations
   sources/Sources



