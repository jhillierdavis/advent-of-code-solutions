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
    assert p.get_x() == 1
    assert p.get_y() == 2

def test_point2d_accessors():
    # Given: a 2-D point
    p = Point2D(1,2)

    # Then: check that the X & Y co-ords are as provided
    assert p.get_x() == 1
    assert p.get_y() == 2

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

import heapq

def test_with_heapq():
    h = []
    heapq.heappush(h, (5, Point2D(0, 1)))
    heapq.heappush(h, (1, Point2D(2,1)))
    heapq.heappush(h, (3, Point2D(1,1)))
    heapq.heappush(h, (3, Point2D(1,0)))
    heapq.heappush(h, (4, Point2D(1,2)))

    #print(f"DEBUG: h={h}") # Sorted list (min. value first)

    assert heapq.heappop(h) == (1, Point2D(2,1))
    assert heapq.heappop(h)[0] == 3
    assert heapq.heappop(h)[0] == 3
    assert heapq.heappop(h)[0] == 4
    assert heapq.heappop(h)[0] == 5
    assert len(h) == 0 


@pytest.mark.parametrize(
    "expected",
    [
        pytest.param((0,0)),        
        pytest.param((2,3)),
        pytest.param((7,1)),
    ],    
)
def test_to_tuple(expected):
    x,y = expected
    p = Point2D(x,y)

    assert expected == p.to_tuple()