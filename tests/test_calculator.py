"""Tests for calculator module."""
import pytest
from src.calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 7) == -7


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    """This test should FAIL — divide() does not handle ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
