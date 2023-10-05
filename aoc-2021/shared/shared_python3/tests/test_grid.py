import pytest # for parameterised tests etc.

from helpers.grid import Grid2D
from helpers.point import Point2D

def test_grid_creation():
    grid = Grid2D(3,2)

    assert grid is not None
    assert type(grid) is Grid2D

def test_grid_creation_invalid_missing_params():
    with pytest.raises(TypeError):
        Grid2D()

def test_grid_creation_invalid_params():
    with pytest.raises(Exception):
        Grid2D(-1,9)

def test_grid_accessors():
    grid = Grid2D(3,2)

    assert grid.getWidth() == 3
    assert grid.getHeight() == 2

def test_grid_coord_symbol_default():
    grid = Grid2D(3,2)

    assert grid.getSymbol(Point2D(1,1)) == '.'  

@pytest.mark.parametrize(
    "point,expected",
    [
        pytest.param(
            Point2D(-1,0), False
        ),
        pytest.param(
            Point2D(0,-1), False
        ),
        pytest.param(
            Point2D(3,1), False
        ),
        pytest.param(
            Point2D(0,0), True
        ),
        pytest.param(
            Point2D(1,1), True
        ),
        pytest.param(
            Point2D(2,1), True
        ),

    ],
)
def test_contains(point, expected):
    # Given: a 2-D grid of (x,y) coord points
    g = Grid2D(3,2)

    # Then: points are contained (or not) as expected
    assert g.contains(point) == expected

def test_cardinal_point_neighbours():
    # Given: a 2-D grid of (x,y) coord points
    g = Grid2D(3,3)

    # Then:
    assert len(g.getCardinalPointNeighbours(Point2D(0,0))) == 2
    assert len(g.getCardinalPointNeighbours(Point2D(1,1))) == 4

def test_surrounding_neighbours():
    # Given: a 2-D grid of (x,y) coord points
    g = Grid2D(3,3)

    # Then:
    assert len(g.getSurroundingNeighbours(Point2D(0,0))) == 3
    assert len(g.getSurroundingNeighbours(Point2D(1,1))) == 8


def test_string_representation():
    # Given: a 2-D grid
    g = Grid2D(3,2)

    # When:
    as_str = str(g)

    # Then: check string representation as expected
    print(f"DEBUG: grid={as_str}")
    assert "Grid2D(id=" in as_str
    assert "width: 3" in as_str
    assert "height: 2" in as_str      
