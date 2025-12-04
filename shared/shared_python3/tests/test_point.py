import pytest

from helpers.point import Point2D, Point3D, Point4D

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


def test_point2d_point2d_accessors():
    # Given: a 2-D point
    p = Point2D(1,2)

    # Then: check that the X & Y co-ords are as provided
    assert p.get_x() == 1
    assert p.get_y() == 2


def test_point2d_string_representation():
    # Given: a 2-D point
    p = Point2D(1,2)

    # When:
    point_as_str = str(p)

    # Then: check an instance is created
    assert "Point2D(id=" in point_as_str
    assert "x: 1" in point_as_str
    assert "y: 2" in point_as_str


def test_point2d_get_closest_neigbours():
    p2d = Point2D(1,1)
    neighbour_set = p2d.get_closest_neighbours()
    
    """
    assert len(neighbour_set) == 8
    assert Point2D(0,0) in neighbour_set
    assert Point2D(1,0) in neighbour_set
    assert Point2D(2,0) in neighbour_set
    assert Point2D(0,1) in neighbour_set
    assert Point2D(2,1) in neighbour_set
    assert Point2D(0,2) in neighbour_set
    assert Point2D(1,2) in neighbour_set
    assert Point2D(2,2) in neighbour_set
    """
    expected_set = ((0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(1,2),(2,2))
    assert len(neighbour_set) == len(expected_set)
    for e in expected_set:
        assert Point2D(e[0], e[1]) in neighbour_set


def test_point2d_equality():
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

def test_point2d_with_heapq():
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
def test_point2d_to_tuple(expected):
    x,y = expected
    p = Point2D(x,y)

    assert expected == p.to_tuple()


@pytest.mark.parametrize(
    "point_a, point_b, expected",
    [
        pytest.param((0,0), (0,0), 0),        
        pytest.param((0,0), (2,3), 5),
        pytest.param((2,3), (7,1), 7),
    ],    
)
def test_point2d_get_manhatten_distance_to(point_a, point_b, expected):
    # Given 2 (2D) points
    p2d_a = Point2D(point_a[0], point_a[1])
    p2d_b = Point2D(point_b[0], point_b[1])

    # Calculate the Manhatten distance between them
    p2d_a.get_manhatten_distance_to(p2d_b) == expected

    # Check that associative 
    p2d_b.get_manhatten_distance_to(p2d_a) == expected


@pytest.mark.parametrize(
    "expected",
    [
        pytest.param((0,0,0)),        
        pytest.param((2,3,4)),
        pytest.param((7,1,-9)),
    ],    
)
def test_point3d_to_tuple(expected):
    x,y,z = expected
    p = Point3D(x,y,z)

    assert expected == p.to_tuple()


@pytest.mark.parametrize(
    "point_a, point_b, expected",
    [
        pytest.param((0,0,0), (0,0,0), 0),        
        pytest.param((0,0,0), (2,3,4), 9),
        pytest.param((2,3,4), (7,1,-9), 20),
    ],    
)
def test_point3d_get_manhatten_distance_to(point_a, point_b, expected):
    # Given 2 (3D) points
    p3d_a = Point3D(point_a[0], point_a[1], point_a[2])
    p3d_b = Point3D(point_b[0], point_b[1], point_b[2])

    # Calculate manhatten distance between them
    p3d_a.get_manhatten_distance_to(p3d_b) == expected   

    # Check that associative 
    p3d_b.get_manhatten_distance_to(p3d_a) == expected


def test_point3d_get_closest_neigbours():
    p3d = Point3D(1,1,1)
    neighbour_set = p3d.get_closest_neighbours()
    assert len(neighbour_set) == 26


def test_point4d_get_closest_neigbours():
    p4d = Point4D(1,1,1,1)
    neighbour_set = p4d.get_closest_neighbours()
    assert len(neighbour_set) == 80
