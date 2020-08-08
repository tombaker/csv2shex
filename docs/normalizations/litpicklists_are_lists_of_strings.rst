Literal picklists as lists
^^^^^^^^^^^^^^^^^^^^^^^^^^

Constraint values of constraint type `LitPicklist` are interpreted as lists.

.. csv-table:: 
   :file: ../normalizations/litpicklist_items_are_strings.csv
   :header-rows: 1

This is interpreted as::

    DCAP
        Shape
            shape_id: :book
            start: True
            Statement
                prop_id: :color
                constraint_value: ['red', 'green', 'yellow']
                constraint_type: LitPicklist
            Statement
                prop_id: :color
                constraint_value: ['red']
                constraint_type: LitPicklist
