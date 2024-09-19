import pytest
from src.calculator import add, subtract, multiply, divide
# from src import calculator 이렇게 작성할 때는 __init__py 라고 각 폴더에 작성해서 명시해야 한다.

def test_add():
    assert add(2, 3) == 5
    assert add(2, -3) == -1
    assert add(4, 4) == 8

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(5, -3) == 8
    assert subtract(5, 5) == 0

def test_multiply():
    assert multiply(10, 0) == 0
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(12, 3) == 4
    assert divide(0, 1) == 0
    with pytest.raises(ValueError):
        divide(1, 0)


