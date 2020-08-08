URI picklists as lists of URIs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Constraint values of constraint type `UriPicklist` are interpreted as lists of strings.

.. csv-table:: 
   :file: ../normalizations/uripicklist_items_are_lists_of_uris.csv
   :header-rows: 1

This is interpreted as::

    DCAP
        Shape
            shape_id: :book
            start: True
            Statement
                prop_id: :color
                constraint_value: [':red', ':green', ':yellow']
                constraint_type: UriPicklist
            Statement
                prop_id: :color
                constraint_value: ['https://example.org/red']
                constraint_type: UriPicklist
