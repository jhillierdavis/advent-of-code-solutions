import pytest # for parameterised tests etc.

import grid2d
import point2d

def test_grid_creation():
    grid = grid2d.Grid2D(3,2)

    assert grid is not None
    assert type(grid) is grid2d.Grid2D

def test_grid_creation_invalid_missing_params():
    with pytest.raises(TypeError):
        grid = grid2d.Grid2D()

def test_grid_creation_invalid_params():
    with pytest.raises(Exception):
        grid = grid2d.Grid2D(-1,9)

def test_grid_accessors():
    grid = grid2d.Grid2D(3,2)

    assert grid.getWidth() == 3
    assert grid.getHeight() == 2

def test_grid_coord_symbol_default():
    grid = grid2d.Grid2D(3,2)

    assert grid.getSymbol(point2d.Point2D(1,1)) == '.'  

@pytest.mark.parametrize(
    "point,expected",
    [
        pytest.param(
            point2d.Point2D(-1,0), False
        ),
        pytest.param(
            point2d.Point2D(0,-1), False
        ),
        pytest.param(
            point2d.Point2D(3,1), False
        ),
        pytest.param(
            point2d.Point2D(0,0), True
        ),
        pytest.param(
            point2d.Point2D(1,1), True
        ),
        pytest.param(
            point2d.Point2D(2,1), True
        ),

    ],
)
def test_contains(point, expected):
    # Given: a 2-D grid of (x,y) coord points
    grid = grid2d.Grid2D(3,2)

    # Then: points are contained (or not) as expected
    assert grid.contains(point) == expected

def test_cardinal_point_neighbours():
    # Given: a 2-D grid of (x,y) coord points
    grid = grid2d.Grid2D(3,3)

    # Then:
    assert len(grid.getCardinalPointNeighbours(point2d.Point2D(0,0))) == 2
    assert len(grid.getCardinalPointNeighbours(point2d.Point2D(1,1))) == 4

def test_surrounding_neighbours():
    # Given: a 2-D grid of (x,y) coord points
    grid = grid2d.Grid2D(3,3)

    # Then:
    assert len(grid.getSurroundingNeighbours(point2d.Point2D(0,0))) == 3
    assert len(grid.getSurroundingNeighbours(point2d.Point2D(1,1))) == 8


def test_string_representation():
    # Given: a 2-D grid
    grid = grid2d.Grid2D(3,2)

    # When:
    as_str = str(grid)

    # Then: check string representation as expected
    print(f"DEBUG: grid={as_str}")
    assert "Grid2D(id=" in as_str
    assert "width: 3" in as_str
    assert "height: 2" in as_str      