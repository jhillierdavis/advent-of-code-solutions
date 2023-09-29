import pytest
import grid2d
import point2d

def test_grid_creation():
    grid = grid2d.Grid2D(3,2)

    assert grid is not None
    assert type(grid) is grid2d.Grid2D

def test_grid_creation_invalid_missing_params():
    with pytest.raises(TypeError):
        grid = grid2d.Grid2D()

def test_grid_creation_invalid_invalid_params():
    with pytest.raises(Exception):
        grid = grid2d.Grid2D(-1,9)

def test_grid_accessors():
    grid = grid2d.Grid2D(3,2)

    assert grid.getWidth() == 3
    assert grid.getHeight() == 2

def test_grid_coord_symbol_default():
    grid = grid2d.Grid2D(3,2)

    assert grid.getSymbol(point2d.Point2D(1,1)) == '.'  

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