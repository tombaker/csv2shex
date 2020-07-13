"""Constants used within the module."""


SHAPE_KEYS = ["start", "shape_id", "shape_label"]

STATEMENT_KEYS = [
    "prop_id",
    "prop_label",
    "mand",
    "repeat",
    "value_type",
    "value_datatype",
    "constraint_value",
    "constraint_type",
    "shape_ref",
    "annot",
]

PREFIXFILE_NAME = "prefixes.yml"

PREFIXFILE_CONTENT = (
    "prefixes:\n"
    "    dc: http://purl.org/dc/elements/1.1/\n"
    "    dcterms: http://purl.org/dc/terms/\n"
    "    dct: http://purl.org/dc/terms/\n"
    "    foaf: http://xmlns.com/foaf/0.1/\n"
    "    skos: http://www.w3.org/2004/02/skos/core#\n"
    "    skosxl: http://www.w3.org/2008/05/skos-xl#\n"
    "    dcat: http://www.w3.org/ns/dcat\n"
    "    xsd: http://www.w3.org/2001/XMLSchema\n"
    "    sx: http://www.w3.org/ns/shex\n"
    "    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#\n"
    "    rdfs: http://www.w3.org/2000/01/rdf-schema#\n"
)

