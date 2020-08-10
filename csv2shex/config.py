"""Constants."""

CONFIGFILE_NAME = ".c2src"

CSV_ELEMENTS = """\
shape_elements:
- shape_id
- shape_label
- start
statement_elements:
- prop_id
- prop_label
- mand
- repeat
- value_type
- constraint_value
- constraint_type
- shape_ref
- annot
"""

ELEMENT_PICKLISTS = """\
value_type:
- URI
- BNode
- Literal
- Nonliteral
constraint_type:
- Datatype
- UriStem
- UriPicklist
- LitPicklist
- LangTag
- LangTagPicklist
- Regex
"""

PREFIXES = """\
prefixes:
    dc: http://purl.org/dc/elements/1.1/
    dcat: http://www.w3.org/ns/dcat
    dct: http://purl.org/dc/terms/
    dcterms: http://purl.org/dc/terms/
    foaf: http://xmlns.com/foaf/0.1/
    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
    rdfs: http://www.w3.org/2000/01/rdf-schema#
    skos: http://www.w3.org/2004/02/skos/core#
    skosxl: http://www.w3.org/2008/05/skos-xl#
    sx: http://www.w3.org/ns/shex
    xsd: http://www.w3.org/2001/XMLSchema
"""
