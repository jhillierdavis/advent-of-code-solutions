import pytest

import solution, ai_solution # Manual & (subsequently created) AI (CoPilot) generated (core algorithm) solutions

input_example = "AOC-2025-Day-01_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-01_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 3),
        pytest.param(input_full, 1180),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value

    # Repeat for AI generated algorithm
    value = ai_solution.solve_part1(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 6),
        pytest.param(input_full, 6892),
    ],    
)
def test_solve_part2(filename, expected):
    # Simple (brute force type) approach 
    value = solution.solve_part2_using_single_unit_increments(filename)    
    assert expected == value

    # Alternative approach using calculated offset
    value = solution.solve_part2_using_modular_arithemtic_offset(filename)    
    assert expected == value

    # Repeat for AI generated algorithm
    value = ai_solution.solve_part2(filename)    
    assert expected == value


# AI generated unit test

# Assuming your function is defined in the same file or imported:
# from your_module import calculate_dial_value_with_zero_clicks

@pytest.mark.parametrize(
    "current, direction, amount, expected",
    [
        (50, 'R', 5,   (55, 0)),
        (52, 'R', 48,  (0, 1)),
        (95, 'R', 10,  (5, 1)),
        (5,  'L', 10,  (95, 1)),
        (5,  'L', 5,   (0, 1)),
        (35, 'L', 36,  (99, 1)),
        (0,  'L', 5,   (95, 0)),
        (30, 'L', 30,  (0, 1)),
        (50, 'L', 68,  (82, 1)),
        (75, 'R', 25,  (0, 1)),
        (10, 'L', 10,  (0, 1)),
        (26, 'R', 74,  (0, 1)),
        (0,  'R', 154, (54, 1)),  # corrected case
        (91, 'L', 829, (62, 8)),
    ]
)
def test_calculate_dial_value_with_zero_clicks(current, direction, amount, expected):
    assert ai_solution.calculate_dial_value_with_zero_clicks(current, direction, amount) == expected