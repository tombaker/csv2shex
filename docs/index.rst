csv2shex (superseded by `tap2shex <https://github.com/tombaker/tap2shex>`_)
===========================================================================

Csv2shex is a command-line utility for reading, interpreting, and verifying CSV files formatted according to the DC Application Profile (DCAP) model. 

This project has been undertaken in parallel to, and in support of, a DCMI working group which is creating the DCAP CSV model [#dcapig]_.

The goals of this project are to make the ShEx data validation language, with its own syntax, accessible to "spreadsheet-enabled" users who are comfortable with tabular formats but do not know the ShEx syntax, and to serve as an "on-ramp" to the more expressive ShEx language by providing an easy way to generate, and to understand, the first draft of a ShEx schema.

.. toctree::
   :maxdepth: 3

   about/About
   install/Install
   cli/Cli
   basics/Basics
   normalizations/Normalizations

.. [#dcapig] https://www.dublincore.org/groups/application_profiles_ig/
