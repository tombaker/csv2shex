"""Class for Python objects derived from CSV files."""

from dataclasses import dataclass, asdict, field
from .exceptions import StatementError


@dataclass
class Shape:
    """Holds state and self-validation methods for a Shape."""

    shapeid: str = None
    is_start_shape: bool = False
    property_values: list = field(default_factory=list)

#        statement_dict = asdict(statement)
#        if statement.shapeid not in shapes:
#            shapes.append(statement)
#            if stat.shapeid not in shapeids:
#                shapeids.append(stat.shapeid)
#            if not shapeids:
#                stat.start = True
#    print(shapes)
#    return shapes


def list_shapes(statements_list):
    """Return list of Shape objects from list of Statement objects."""
    # statements = [asdict(s) for s in statements_list]
    shapes = []
    for statement in statements_list:
        print(statements_list)
        
