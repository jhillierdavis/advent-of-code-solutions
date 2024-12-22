import pytest

import solution

input_example = "AOC-2024-Day-22_Puzzle-Input-Example.txt"
input_example_part2 = "AOC-2024-Day-22_Puzzle-Input-Example-Part2.txt"
input_full = "AOC-2024-Day-22_Puzzle-Input-Full.txt"


@pytest.mark.parametrize(
    "initial, mixin, expected",
    [
        pytest.param(42, 15, 37),
    ],    
)
def test_mix(initial, mixin, expected):
    value = solution.mix(initial, mixin)    
    assert expected == value

@pytest.mark.parametrize(
    "initial, expected",
    [
        pytest.param(100000000, 16113920),
    ],    
)
def test_prune(initial, expected):
    value = solution.prune(initial)    
    assert expected == value
    


@pytest.mark.parametrize(
    "initial, max, expected",
    [
        pytest.param(123, 1, [15887950]),
        pytest.param(123, 10, [15887950, 16495136, 527345, 704524, 1553684, 12683156, 11100544, 12249484, 7753432, 5908254]),
    ],    
)
def test_generate_secret_number_sequence(initial, max, expected):
    value = solution.generate_secret_number_sequence(initial, max)
    
    assert expected == value

@pytest.mark.parametrize(
    "initial, n, expected",
    [
        pytest.param(123, 1, 15887950),
        pytest.param(123, 10, 5908254),
        pytest.param(1, 2000, 8685429),
        pytest.param(10, 2000, 4700978),
        pytest.param(100, 2000, 15273692),
        pytest.param(2024, 2000, 8667524),
    ],    
)
def test_generate_nth_secret_number(initial, n, expected):
    value = solution.generate_nth_secret_number(initial, n)    
    assert expected == value



#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 37327623),
        pytest.param(input_full, 15608699004), # Ignore for speed
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value



@pytest.mark.parametrize(
    "initial, max, expected",
    [
        pytest.param(123, 10, [3,0,6,5,4,4,6,4,4,2]),
    ],    
)
def test_generate_secret_number_price_sequence(initial, max, expected):
    value = solution.generate_secret_number_price_sequence(initial, max)    
    assert expected == value

@pytest.mark.parametrize(
    "number_sequence, expected",
    [
        pytest.param([3,0,6,5,4,4,6,4,4,2], [-3,6,-1,-1,0,2,-2,0,-2]),
    ],    
)
def test_get_change_sequence(number_sequence, expected):
    value = solution.get_change_sequence(number_sequence)    
    assert expected == value


@pytest.mark.parametrize(
    "secret_number, max, changes, expected",
    [
        pytest.param(123, 10, [-1,-1,0,2], 6),
    ],    
)
def test_get_price_point_matching_change_sequence(secret_number, max, changes, expected):
    assert expected == solution.get_price_point_matching_change_sequence(secret_number, max, changes)


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [        
        pytest.param(input_example_part2, 23),
        pytest.param(input_example, 24),
        pytest.param(input_full, 1791),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
