"""Defines a base class to be used in the testing."""
import abc


class Base(abc.ABC):
    """Define a base class to be used in the testing."""

    class_var = None

    @abc.abstractmethod
    def funsies() -> None:
        """Force children do something pointless."""
