Minimal DCAP
^^^^^^^^^^^^

The most minimal application profile simply provides a list of properties used.

.. csv-table:: 
   :file: ../basics/propid.csv
   :header-rows: 1

Interpreted as::

    DCAP
        Shape
            shapeID: @default
            start: True
            Statement
                prop_id: dct:creator
            Statement
                prop_id: dct:title
            Statement
                prop_id: dct:publisher
            Statement
                prop_id: dct:date
