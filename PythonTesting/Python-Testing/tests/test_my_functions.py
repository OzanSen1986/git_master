import pytest
from source.my_functions import add, divide
import time


def test_add():
    result = add(10, 16)
    assert result == 26

def test_divide() -> None:
    result = divide(100,2)
    assert result == 50

def test_divide_by_zero() -> None:
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = divide(100,2)
    assert result == 50

@pytest.mark.skip(reason="this feature is currently broken.")
def test_add():
    assert add(1, 2) == 3

@pytest.mark.xfail(reason="we know we can not divide by zero")
def test_divide_zero_broken():
    divide(4, 0)

    







