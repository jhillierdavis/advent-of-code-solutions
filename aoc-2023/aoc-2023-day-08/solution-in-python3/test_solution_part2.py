import pytest

import solution_part2

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param("puzzle-input-example-part2.txt", 6),
        pytest.param("puzzle-input-full.txt", 9858474970153), # 265062770423925 too high!
    ],    
)
def test_solution_part2(input, expected):
    assert solution_part2.solve(input) == expected