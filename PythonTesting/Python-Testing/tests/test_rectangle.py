import pytest
from source import shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def my_second_rectangle() -> None:
    return shapes.Rectangle(5, 6)


def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 + 20) * 2

def test_not_equal():
    assert my_rectangle != my_second_rectangle

