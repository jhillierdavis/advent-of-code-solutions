import pytest

import solution

input_example = "AOC-2025-Day-12_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-12_Puzzle-Input-Full.txt"


example_shape_map = {0: ['###', '##.', '##.'], 1: ['###', '##.', '.##'], 2: ['.##', '###', '##.'], 3: ['##.', '###', '##.'], 4: ['###', '#..', '###'], 5: ['###', '.#.', '###']}

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "fit_requirements, expected",
    [
        pytest.param("4x4: 0 0 0 0 2 0", True),
        pytest.param("12x5: 1 0 1 0 2 2", True),
        pytest.param("12x5: 1 0 1 0 3 2", False),
    ],    
)
def test_can_fit_required_shapes(fit_requirements, expected):
    value = solution.can_fit_required_shapes(example_shape_map, fit_requirements)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 2),
        pytest.param(input_full, -1),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, -1),
        #pytest.param(input_full, -1),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
