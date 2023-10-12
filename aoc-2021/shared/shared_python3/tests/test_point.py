import pytest

from helpers.point import Point2D

@pytest.mark.parametrize(
    "x,y",
    [
        pytest.param('a', 0),
        pytest.param(1, 'b'),
        pytest.param('x', 'y'),
    ],    
)
def test_point2d_invalid_creation(x,y):
    with pytest.raises(TypeError):
        p = Point2D(x,y)


def test_point2d_valid_creation():
    # Given: a 2-D point
    p = Point2D(1,2)

    # Then: check an instance is created
    assert p is not None
    assert type(p) is Point2D
    assert p.getX() == 1
    assert p.getY() == 2

def test_point2d_accessors():
    # Given: a 2-D point
    p = Point2D(1,2)

    # Then: check that the X & Y co-ords are as provided
    assert p.getX() == 1
    assert p.getY() == 2

def test_string_representation():
    # Given: a 2-D point
    p = Point2D(1,2)

    # When:
    point_as_str = str(p)

    # Then: check an instance is created
    assert "Point2D(id=" in point_as_str
    assert "x: 1" in point_as_str
    assert "y: 2" in point_as_str

def test_equality():
    # Given: non-identical, but equal 
    pa = Point2D(1,2)
    pb = Point2D(1,2)
    pc = Point2D(2,2)

    # Then: not identical as expected
    assert pa is not pb
    assert pa is not pb

    # And: equality as expected
    assert pa == pb
    assert pa != pc
