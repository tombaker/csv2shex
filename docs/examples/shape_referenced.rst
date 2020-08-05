Named shapes, referenced
^^^^^^^^^^^^^^^^^^^^^^^^

A statement may include a reference back to a shape to which the object value of a property must conform.

.. csv-table:: 
   :file: ../examples/shape_referenced.csv
   :header-rows: 1

Interpreted as::

    DCAP
        Shape
            shape_id: :book
            start: True
            Statement
                prop_id: dct:creator
                shape_ref: @:person
        Shape
            shape_id: :person
            Statement
                prop_id: foaf:name

This means:

* A book, as described according to the `:book` shape, has a creator.
* The creator of the book must be described in accordance with the `:person` shape.
* The `:person` shape says that the description of a person must include their name.

Note that only the first shape is flagged as a 'start' shape.
