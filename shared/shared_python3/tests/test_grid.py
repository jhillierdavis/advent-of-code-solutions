import pytest # for parameterised tests etc.

from helpers.grid import Grid2D
from helpers.grid import display_grid
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

    assert grid.get_width() == 3
    assert grid.get_height() == 2

def test_grid_coord_symbol_default():
    grid = Grid2D(3,2)

    assert grid.get_symbol(Point2D(1,1)) == '.'  

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
    assert len(g.get_cardinal_point_neighbours(Point2D(0,0))) == 2
    assert len(g.get_cardinal_point_neighbours(Point2D(1,1))) == 4

def test_surrounding_neighbours():
    # Given: a 2-D grid of (x,y) coord points
    g = Grid2D(3,3)

    # Then:
    assert len(g.get_surrounding_neighbours(Point2D(0,0))) == 3
    assert len(g.get_surrounding_neighbours(Point2D(1,1))) == 8


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

def create_populated_test_grid():
    g = Grid2D(3,4)

    # Populate grid
    i = 0
    for x in range(g.get_width()):
        for y in range(g.get_height()):            
            p = Point2D(x,y)
            g.set_symbol(p, i)
            i += 1

    return g


def test_get_subgrid_from_orgin():
    # Given: a test grid
    g = create_populated_test_grid()

    # When: subgrid created
    sg = g.get_subgrid_from_origin(g.get_width() - 1 , g.get_height() - 1)

    # Then:
    assert sg.get_width() == 2
    assert sg.get_height() == 3
    assert sg.get_symbol(Point2D(0,0)) == 0
    assert sg.get_symbol(Point2D(1,2)) == 6


def test_get_subgrid_inclusive():
    # Given: a test grid
    g = create_populated_test_grid()

    # When: subgrid created
    sg = g.get_subgrid_inclusive(Point2D(1,1), Point2D(2,3))
    #print(f"DEBUG: sg = {sg}")

    # Then:
    assert sg.get_width() == 2
    assert sg.get_height() == 3
    assert sg.get_symbol(Point2D(0,0)) == 5
    assert sg.get_symbol(Point2D(1,2)) == 11


def test_get_inverted_vertically():  
    # Given: a test grid
    g = create_populated_test_grid()

    # When
    ig = g.get_inverted_vertically()

    #print(f"DEBUG: {g}")
    #display_grid(g)
    #print(f"DEBUG: {ig}")
    #display_grid(ig)

    # Then:
    assert g.get_symbol(Point2D(0,0)) == 0
    assert ig.get_symbol(Point2D(0,0)) == 3
    assert g.get_symbol(Point2D(2,3)) == 11
    assert ig.get_symbol(Point2D(2,3)) == 8


def test_get_inverted_horizontally():  
    # Given: a test grid
    g = create_populated_test_grid()

    # When
    ig = g.get_inverted_horizontally()

    # Then:
    assert g.get_symbol(Point2D(0,0)) == 0
    assert ig.get_symbol(Point2D(0,0)) == 8
    assert g.get_symbol(Point2D(2,3)) == 11
    assert ig.get_symbol(Point2D(2,3)) == 3

def test_count():
    # Given: a grid instance
    g = Grid2D(3,4)

    # Then: populated with symbols
    g.set_symbol(Point2D(0,0), '#')
    g.set_symbol(Point2D(1,0), '#')
    g.set_symbol(Point2D(0,1), '#')

    assert g.count_symbol("#") == 3

def test_merge():
    # Given: two grid instances
    hg = Grid2D(3,3)
    vg = Grid2D(3,3)

    # And: populated with symbols
    vg.set_symbol(Point2D(1,0), '#')
    vg.set_symbol(Point2D(1,1), '#')
    vg.set_symbol(Point2D(1,2), '#')
    hg.set_symbol(Point2D(0,1), '#')
    hg.set_symbol(Point2D(1,1), '#')
    hg.set_symbol(Point2D(2,1), '#')

    # Then:
    assert hg.count_symbol('#') == 3

    # When:
    hg.merge_symbol(vg, '#')
    assert hg.count_symbol('#') == 5


def test_clone_and_equals():
    # Given: a test grid
    g = create_populated_test_grid()

    # When: cloned
    cloned = g.clone()

    # Then: not identical
    assert g is not cloned

    # But: equal (same symbol values at each equivalent point)
    assert g == cloned

@pytest.mark.parametrize(
    "start_coord, expected_coord, expected_symbol",
    [
        pytest.param((1,2), (2,2), 10),
        pytest.param((3,0), None, None),
    ],    
)
def test_get_neighbour_east(start_coord, expected_coord, expected_symbol):
    # Given: a test grid
    g = create_populated_test_grid()
    #display_grid(g)

    # Then:
    right = g.get_neighbour_point_east(Point2D(start_coord[0], start_coord[1]))
    if None != expected_coord:
        assert right == Point2D(expected_coord[0], expected_coord[1])
        assert g.get_symbol(right) == expected_symbol
    else:
        assert right == None

@pytest.mark.parametrize(
    "start_coord, expected_coord, expected_symbol",
    [
        pytest.param((1,2), (0,2), 2),
        pytest.param((0,1), None, None),
    ],    
)
def test_get_neighbour_point_west(start_coord, expected_coord, expected_symbol):
    # Given: a test grid
    g = create_populated_test_grid()
    #display_grid(g)

    # Then:
    right = g.get_neighbour_point_west(Point2D(start_coord[0], start_coord[1]))
    if None != expected_coord:
        assert right == Point2D(expected_coord[0], expected_coord[1])
        assert g.get_symbol(right) == expected_symbol
    else:
        assert right == None

@pytest.mark.parametrize(
    "start_coord, expected_coord, expected_symbol",
    [
        pytest.param((1,2), (1,1), 5),
        pytest.param((1,0), None, None),
    ],    
)
def test_get_neighbour_point_north(start_coord, expected_coord, expected_symbol):
    # Given: a test grid
    g = create_populated_test_grid()
    #display_grid(g)

    # Then:
    right = g.get_neighbour_point_north(Point2D(start_coord[0], start_coord[1]))
    if None != expected_coord:
        assert right == Point2D(expected_coord[0], expected_coord[1])
        assert g.get_symbol(right) == expected_symbol
    else:
        assert right == None


@pytest.mark.parametrize(
    "start_coord, expected_coord, expected_symbol",
    [
        pytest.param((1,2), (1,3), 7),
        pytest.param((1,3), None, None),
    ],    
)
def test_get_neighbour_point_south(start_coord, expected_coord, expected_symbol):
    # Given: a test grid
    g = create_populated_test_grid()
    #display_grid(g)

    # Then:
    right = g.get_neighbour_point_south(Point2D(start_coord[0], start_coord[1]))
    if None != expected_coord:
        assert right == Point2D(expected_coord[0], expected_coord[1])
        assert g.get_symbol(right) == expected_symbol
    else:
        assert right == None
