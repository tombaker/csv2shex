"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field, asdict

# PVPAIR_KEYS = [
#     "prop_id",
#     "prop_label",
#     "mand",
#     "repeat",
#     "value_type",
#     "value_datatype",
#     "constraint_value",
#     "constraint_type",
#     "shape_ref",
#     "annot",
# ]

PVPAIR_KEYS = ["prop_id", "value_type"]


@dataclass
class Shape:
    """Holds state and self-validation methods for a Shape."""

    start: bool = False
    shape_id: str = None
    shape_label: str = None
    shape_pvpairs: list = field(default_factory=list)


def list_shapes(statements_list):
    """Return list of Shape objects from list of Statement objects."""
    shapes_list = list()
    shap = Shape()
    shape_pvpairs_item = dict()
    for statement in statements_list:
        statement = asdict(statement)
        # breakpoint()
        # if new shape is encountered
        if shap.shape_id != statement["shape_id"]:
            # if shap.shape_id is not None
            if shap.shape_id:
                shapes_list.append(shap)
            shap = Shape()
            shap.start = statement["start"]
            shap.shape_id = statement["shape_id"]
            shap.shape_label = statement["shape_label"]

        for pvpair_key in PVPAIR_KEYS:
            shape_pvpairs_item[pvpair_key] = statement[pvpair_key]

        shap.shape_pvpairs.append(shape_pvpairs_item)
        shape_pvpairs_item = dict()
    shapes_list.append(shap)
    return shapes_list
