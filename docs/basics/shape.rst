Named shapes (in own row)
"""""""""""""""""""""""""

A shape can be identified and labeled on its own row. The shape will apply to all subsequent valid rows until a row with a different shape identifier is encountered. The `csv2shex` parser considers the first shape encountered in a CSV file to be the 'start' shape.

.. csv-table:: 
   :file: ../basics/shape.csv
   :header-rows: 1

Interpreted as::

    DCAP
        Shape
            shape_id: :book
            start: True
            Statement
                prop_id: dct:creator
            Statement
                prop_id: dct:title
