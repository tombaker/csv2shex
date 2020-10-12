"""Constants."""

CONFIGFILE_NAME = ".c2src"

CSV_ELEMENTS = """\
shape_elements:
- shapeID
- shapeLabel
- start
statement_elements:
- prop_id
- prop_label
- mand
- repeat
- value_node_type
- value_datatype
- value_constraint
- value_constraint_type
- value_shape
- note
"""

ELEMENT_PICKLISTS = """\
value_node_type:
- URI
- BNode
- Literal
- Nonliteral
value_constraint_type:
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
    : http://example.org/
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
    xsd: http://www.w3.org/2001/XMLSchema#
    wd: https://www.wikidata.org/wiki/
"""
