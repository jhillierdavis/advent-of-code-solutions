import pytest

import solution

@pytest.mark.parametrize(
    "time, distance, combinations",
    [
        pytest.param(7, 9, 4),
        pytest.param(15, 40, 8),
        pytest.param(30, 200, 9),
        pytest.param(52, 426, 31),  # 4 * 8 * 9 = 288
        pytest.param(94, 1374, 57),
        pytest.param(75, 1279, 22),
        pytest.param(94, 1216, 63), # 31 * 57 * 22 * 63 = 2449062
        pytest.param(71530, 940200, 71503),
        #pytest.param(52947594, 426137412791216, 0),
    ],    
)
def test_solution(time, distance, combinations):
    assert solution.solve(time, distance) == combinations    
