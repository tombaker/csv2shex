"""Class for Python objects derived from CSV files."""

from dataclasses import dataclass, asdict, field
from .exceptions import StatementError

# start: bool = False
# shape_id: str = None
# shape_label: str = None
# prop_id: str = None
# prop_label: str = None
# mand: str = None
# repeat: str = None
# value_type: str = None
# value_datatype: str = None
# constraint_value: str = None
# constraint_type: str = None
# shape_ref: str = None
# annot: str = None


@dataclass
class Shape:
    """Holds state and self-validation methods for a Shape."""

    start: bool = False
    shape_id: str = None
    shape_label: str = None
    property_values: list = field(default_factory=list)


def list_shapes(statements_list):
    """Return list of Shape objects from list of Statement objects."""
    # statements_as_dicts = [asdict(s) for s in statements_list]
    # for statement in statements_as_dicts:
    shapes_list = list()
    shap = Shape()
    row_dict = dict()
    for statement in statements_list:
        """When new shape_id, append Shape to shapes_list and initialize new Shape."""
        if shap.shape_id != statement.shape_id:
            if shap.shape_id is not None:
                shapes_list.append(shap)
            shap = Shape()
            shap.start = statement.start
            shap.shape_id = statement.shape_id
            shap.shape_label = statement.shape_label
            shap.property_values = list()
        row_dict["prop_id"] = statement.prop_id
        row_dict["value_type"] = statement.value_type
        shap.property_values.append(row_dict)
        row_dict = dict()
    shapes_list.append(shap)
    return shapes_list
        
