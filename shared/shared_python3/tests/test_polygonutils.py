import pytest

from helpers.polygonutils import calculate_polygon_area_from

@pytest.mark.parametrize(
    "coords,expected",
    [
        pytest.param([(0,0), (4,0), (4,5), (0,5), (0,0)], 20),
        pytest.param([(0,0), (4,0), (4,5), (0,5)], 20),
        pytest.param([(1,1), (4,1), (4,4), (1,4), (1,1)], 9),
    ],    
)
def test_calculate_polygon_area_from(coords, expected):
    assert calculate_polygon_area_from(coords) == expected

