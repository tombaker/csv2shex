Mandatory and repeatable
^^^^^^^^^^^^^^^^^^^^^^^^

The cardinality elements `mand` ("mandatory") and `repeat` ("repeatable") are both by default False. Specifying any value for either element makes that element True.

.. csv-table:: 
   :file: ../normalizations/mandrepeat.csv
   :header-rows: 1

This is interpreted as::

    DCAP
        Shape
            shape_id: @default
            start: True
            Statement
                prop_id: dc:creator
                mand: False
                repeat: True
            Statement
                prop_id: dc:date
                mand: True
                repeat: False

Note that string values such as "No", "N", "n", "0", or "False" will be interpreted as True.

.. csv-table:: 
   :file: ../normalizations/mandrepeat2.csv
   :header-rows: 1

This is interpreted as::

    DCAP
        Shape
            shape_id: @default
            start: True
            Statement
                prop_id: dc:subject
                mand: True
                repeat: True
