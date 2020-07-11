"""Class for Python objects derived from CSV files."""

from dataclasses import dataclass, asdict, field
from .exceptions import StatementError

property_value_fields = []

@dataclass
class Shape:
    """Holds state and self-validation methods for a Shape."""

    start: bool = False
    shape_id: str = None
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
            shap.property_values = list()
        row_dict["prop_id"] = statement.prop_id
        row_dict["value_type"] = statement.value_type
        shap.property_values.append(row_dict)
        row_dict = dict()
    shapes_list.append(shap)
    return shapes_list
        

#        statement_dict = asdict(statement)
#        if statement.shape_id not in shapes:
#            shapes.append(statement)
#            if stat.shape_id not in shape_ids:
#                shape_ids.append(stat.shape_id)
#            if not shape_ids:
#                stat.start = True
#    print(shapes)
#    return shapes
