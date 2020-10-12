Picklists of URIs
^^^^^^^^^^^^^^^^^

Constraint values of constraint type `UriPicklist` are interpreted as lists of URIs or prefixed URIs.

.. csv-table:: 
   :file: ../normalizations/uripicklists.csv
   :header-rows: 1

This is interpreted as::

    DCAP
        Shape
            shapeID: :book
            start: True
            Statement
                prop_id: :color
                constraint_value: [':red', ':green', ':yellow']
                constraint_type: UriPicklist
            Statement
                prop_id: :color
                constraint_value: ['https://example.org/red']
                constraint_type: UriPicklist
