URIs stripped of angle brackets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If URIs are enclosed URIs in angle brackets, the brackets are stripped away.

.. csv-table:: 
   :file: ../normalizations/uris_minus_angle_brackets.csv
   :header-rows: 1

This is interpreted as::

    DCAP
        Shape
            shape_id: :book
            start: True
            Statement
                prop_id: dct:subject
                constraint_value: https://id.loc.gov/subjects
                constraint_type: UriStem
            Statement
                prop_id: dct:creator
                value_type: URI
                constraint_value: https://www.wikidata.org/wiki/Q46914185
