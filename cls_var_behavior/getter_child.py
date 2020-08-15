"""Define a class to modify the base class's class variable."""
from __future__ import annotations

from typing import Any

from .base import Base


class GetterChild(Base):
    """Read Base's class variable."""

    def get_base_class_var(self: GetterChild) -> Any:
        """Get the value of the base class's class_var."""
        print(f'Value of class_var: "{Base.class_var}"')
        return Base.class_var

    def funsies() -> None:
        """Implement abstract class."""
        pass
