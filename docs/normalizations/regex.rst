Regular expressions
^^^^^^^^^^^^^^^^^^^

When a constraint type of Regex is specified, the corresponding constraint value is normalized as follows:

- csv2shex will try to replace the value with a compiled Python regular expression for value. 
- If the value does not compile correctly (e.g., because it is malformed), csv2shex will replace the constraint value with None so as not to pass a bad regular expression to processes or applications downstream.
- If no constraint constraint value is specified, csv2shex will leave it unspecified.

.. csv-table:: 
   :file: ../normalizations/regex.csv
   :header-rows: 1

This is interpreted as::

    DCAP
        Shape
            shape_id: @default
            start: True
            Statement
                prop_id: :status
                value_type: Literal
                constraint_value: re.compile('approved_*')
                constraint_type: Regex
            Statement
                prop_id: :status
                value_type: Literal
                constraint_type: Regex
            Statement
                prop_id: :status
                value_type: Literal
                constraint_type: Regex
            Statement
                prop_id: :status
                value_type: Literal
                constraint_value: re.compile('/approved_*/')
                constraint_type: Regex
            Statement
                prop_id: :status
                value_type: Literal
                constraint_value: re.compile('^2020 August')
                constraint_type: Regex

Note:

- For the third statement, csv2shex drops the malformed constraint value and displays an error message::

    'approved_(*' is not a valid (Python) regular expression.

- While regular expressions are commonly enclosed in forward slashes, csv2shex reads the forward slashes as part of the regular expression. In other words, `re.compile('/NOW/')` will match the string `/NOW/`. Enclosing quotes will also be considered part of the regular expression, so a constraint value of `'NOW'` will be normalized as `re.compile("'NOW'")`.

- Regular expressions can include spaces.

- The Regex constraint typically applies to a Literal constraint value, so where a value type has been left unspecified, csv2shex will assign to it the value 'Literal'. However, where a different value type has already been assigned (eg, URI or BNode), csv2shex will leave the assigned value unchanged; the user is responsible for catching such errors.
