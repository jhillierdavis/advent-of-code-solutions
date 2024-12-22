import pytest

import solution

input_example = "AOC-2024-Day-22_Puzzle-Input-Example.txt"
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
        pytest.param(input_full, 'TODO'),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 'TODO'),
        #pytest.param(input_full, 'TODO'),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
