import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", [3,7]),
    ],    
)
def test_get_empty_rows_from_filename(filename, expected):
    assert solution.get_empty_rows_from_filename(filename) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", [2,5,8]),
    ],    
)
def test_get_empty_columns_from_filename(filename, expected):
    assert solution.get_empty_columns_from_filename(filename) == expected



@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", -1),
    ],    
)
def test_solution(filename, expected):
    assert solution.solve(filename) == expected