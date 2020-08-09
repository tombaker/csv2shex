csv2shex
========

Csv2shex is a command-line utility for reading, interpreting, and verifying CSV files formatted according to the DC Application Profile (DCAP) model. The utility interprets and normalizes the contents of a CSV files and prints the results to standard outpus as an aid for debugging. The utility also converts the CSV contents into a YAML representation that is intended to be used for generating schemas in ShEx (and in principle in other such validation languages).

This project has been undertaken in parallel to, and in support of, a working group of the Dublin Core Metadata Initiative which is creating the DCAP model (@@@add links).

The aim of this work to support the creation of simple validation schemas by means of a tabular format that is accessible to "spreadsheet-enabled" users. The tabular format, it is hoped, will serve as an "on-ramp" to real validation languages by providing an easy way to generate the first draft of a schema in ShEx. The code in this project tries to anticipate messy or incomplete CSV inputs and to fill gaps and normalize inconsistencies during the transformation into YAML. For example, the code allows users to enter URIs either as full URIs (with or without enclosing angle brackets) or as abbreviated URIs written with namespace prefixes (e.g., 'dcterms:creator'), or to enter the datatypes of literal values without using an extra column to specify that the value is a Literal (since this can be inferred).

Work both in this project and in the context of the DCMI working group has focused on defining the "elements" (concretely: the fixed set of CSV column headers) of the DCAP model. As of August 2020, the nature and definition of these elements is still somewhat in flux, so the descriptions provided in this documentation should be considered provisional.

Our hope is that a simple, well-defined model, expressible in CSV and convertible into YAML, will provide a solid basis for generating validation schemas in ShEx.

It is also our hope that modules and Python classes on which this command-line utility can be adapted for use in other environments. This documentation explains how CSV files are interpreted and normalized. For an up-to-the-minute look at how the modules and classes work, the reader is invited to inspect (and execute) the pytest unit tests, which have been formulated for ease of comprehension.

Potential directions for the further development of this project include:

- Resolution of prefixed URIs to full URIs on the basis of a table of namespace prefixes.

- The ability to tweak built-in defaults in local configuration files.

- Namespace prefixes should be readable from sources on the Web or from local configuration files.

- Round-tripping from a messy, first-draft CSV expression of a DCAP, via a normalized expression in Python, to an expression in YAML, then (potentially) back to a normalized expression in CSV.

- Writing the Python expression of a DCAP to an Excel spreadsheet, potentially with tabs for namespace prefixes and controlled sets of values (such as the four main value types URI, Literal, Nonliteral, and BNode) linked to specific columns of the main sheet for use as dropdown menus.

To complete the conversion of CSV into ShEx, the next big task of this work will be to work out how the elements of the DCAP model interface with existing Python modules for generating ShEx schemas.

.. toctree::
   :maxdepth: 3

   install/Install
   install/Command_line
   basics/Basics
   normalizations/Normalizations
   sources/Sources



