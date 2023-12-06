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
        #pytest.param(52947594, 426137412791216, 0), # Too slow!
    ],    
)
def test_wins_using_brute_force_approach(time, distance, combinations):
    assert solution.calculate_wins_using_brute_force_approach(time, distance) == combinations    

@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([(7, 9), (15, 40), (30, 200)], 288), # 4 * 8 * 9 = 288
        pytest.param([(52, 426), (94, 1374), (75, 1279), (94, 1216)], 2449062),  # 31 * 57 * 22 * 63 = 2449062
    ],    
)
def test_solution_part1(values, expected):
    ans = 1
    for v in values:
        ans *= solution.calculate_wins_using_optimised_brute_force_approach(v[0], v[1])
    assert ans == expected


@pytest.mark.parametrize(
    "time, distance, combinations",
    [
        pytest.param(7, 9, 4),
        pytest.param(15, 40, 8),
        pytest.param(30, 200, 9),
        pytest.param(52, 426, 31),  
        pytest.param(94, 1374, 57),
        pytest.param(75, 1279, 22),
        pytest.param(94, 1216, 63),
        pytest.param(71530, 940200, 71503),
        pytest.param(52947594, 426137412791216, 33149631),
    ],    
)
def test_solution_part2(time, distance, combinations):
    assert solution.calculate_wins_using_optimised_brute_force_approach(time, distance) == combinations    

