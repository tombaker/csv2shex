"""Class for Python objects derived from CSV files."""

from dataclasses import dataclass, asdict, field
from .exceptions import StatementError


@dataclass
class Shape:
    """Holds state and self-validation methods for a Shape."""

    shape_id: str = None
    is_start_shape: bool = False
    property_value_pairs: list = field(default_factory=list)

#    shape_id: str = None
#    prop_id: str = None
#    value_type: str = None


#    shape_ids = []
#    print(statements_list)
#    print(statements)
#    return statements

#        statement_dict = asdict(statement)
#        if statement.shape_id not in shapes:
#            shapes.append(statement)
#            if stat.shape_id not in shape_ids:
#                shape_ids.append(stat.shape_id)
#            if not shape_ids:
#                stat.start = True
#    print(shapes)
#    return shapes


def list_shapes(statements_list):
    """Return list of Shape objects from list of Statement objects."""
    statements = [asdict(s) for s in statements_list]
    shapes = []
    for statement in statements:
        pass
