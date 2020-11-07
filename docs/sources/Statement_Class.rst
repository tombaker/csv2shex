CSVRow class
^^^^^^^^^^^^^^^

As defined in the DC Application Profile model (DCAP), a CSVRow is a property-value pair in the context of a Shape. An instance of the class :class:`csv2shex.csvrow.CSVRow`:

* holds, as attributes, data elements and annotations that describe a property-value pair (aka, "statement") as listed in a single row of the CSV representation of a DC Application Profile.
* holds, as attribute, the identifier of the shape to which the statement belongs and a Boolean flag indicating whether it is a "start" shape.
* provides methods for self-validing conformance with the DCAP model and prints warnings or exits with error messages as required.

.. autoclass:: csv2shex.csvrow.CSVRow
    :members:

