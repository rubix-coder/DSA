import pytest
from adder import add
def test_add_integers():
    assert add(1, 2) == 3 
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_add_floats():
    assert add(1.5, 2.5) == 4.0
    assert add(1.1, 2.2) == pytest.approx(3.3)

def test_add_strings():
    with pytest.raises(TypeError):
        add('a', 'b')