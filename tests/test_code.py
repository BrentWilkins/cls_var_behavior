"""Define a set of tests for the cls_var_behavior package."""
import pytest

from cls_var_behavior.base import Base
from cls_var_behavior.getter_child import GetterChild
from cls_var_behavior.setter_child import SetterChild


def test_base_class_cannot_be_instantiated() -> None:
    """Make sure the base class is abstract."""
    with pytest.raises(TypeError, match=r"Can't instantiate abstract class*"):
        Base()


def test_setter_child_class_can_be_instantiated() -> None:
    """Make sure the setter child class can be instantiated."""
    assert SetterChild()


def test_getter_child_class_can_be_instantiated() -> None:
    """Make sure the setter child class can be instantiated."""
    assert GetterChild()


def test_setter_child_class_can_set_cls_var() -> None:
    """Verify that the class variable can be changed."""
    assert Base.class_var is None, 'Class variable should initially be None'

    obj = SetterChild()
    new_value = 'New value'
    obj.set_base_class_var(new_value)
    assert obj.class_var == new_value, 'New value failed to be set'


def test_getter_child_class_gets_value_from_previous_test_not_none() -> None:
    """Verify that if all we do is get, the class variable should be None."""
    obj = GetterChild()
    assert obj.get_base_class_var() is not None, "Setting value in parent class in previous test didn't stick"


def test_setter_and_getter_classes_share_base_var() -> None:
    """Verify that the class variable is shared between child classes."""
    set_obj = SetterChild()
    get_obj = GetterChild()
    shared_value = 'Shared value'

    set_obj.set_base_class_var(shared_value)
    assert get_obj.get_base_class_var() == shared_value, ("Both child classes from same parent class don't"
                                                          ' share the same value')


def test_del_effects_on_modified_base_class() -> None:
    """Show bug in pytest (?) by haveing the del keyword cause an exception."""
    with pytest.raises(UnboundLocalError, match=r"local variable 'Base' referenced before assignment"):
        del Base
