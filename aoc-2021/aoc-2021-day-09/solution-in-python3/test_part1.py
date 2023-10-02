import pytest # for parameterised tests

import part1 as solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param(
            "puzzle-input-example.txt", 15
        ),
        pytest.param(
            "puzzle-input-full.txt", 558
        ),
    ],
)
def test_part1(filename, expected):
    assert solution.sum_low_points_from_file(filename) == expected