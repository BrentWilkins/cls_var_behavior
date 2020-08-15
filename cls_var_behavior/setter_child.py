"""Define a class to modify the base class's class variable."""
from __future__ import annotations

from typing import Any

from .base import Base


class SetterChild(Base):
    """Modify Base's class variable."""

    def set_base_class_var(self: SetterChild, new_val: Any) -> None:
        """Set the value of the base class's class_var to new_val."""
        Base.class_var = new_val
        print(f'New value of class_var: "{Base.class_var}"')

    def funsies() -> None:
        """Implement abstract class."""
        pass
