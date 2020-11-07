"""Defaults."""


CSV_MODEL = """\
shape_elements:
- shapeID
- shapeLabel
- shapeClosed
- start

statement_elements:
- propertyID
- propertyLabel
- mandatory
- repeatable
- valueNodeType
- valueDataType
- valueConstraint
- valueConstraintType
- valueShape
- note

shape_uri_elements:
- shapeID

statement_uri_elements:
- propertyID
- valueDataType
- valueConstraint
- valueShape
"""

DEFAULT_CONFIGFILE_NAME = ".csv2rc"

DEFAULT_CONFIG_SETTINGS_YAML = """\
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
    wdt: http://www.wikidata.org/prop/direct/

valueNodeType:
- URI
- BNode
- Literal
- Nonliteral

valueConstraintType:
- Datatype
- UriStem
- UriPicklist
- LitPicklist
- LangTag
- LangTagPicklist
- Regex
"""
