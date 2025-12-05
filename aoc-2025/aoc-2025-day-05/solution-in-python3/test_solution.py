import pytest

# Unit tests for manual & (subsequently) AI (CoPilot at https://copilot.microsoft.com ) generated (core algorithm) solutions.
# Re-solved (using AI) to refine prompting skill & explore current AI caperbilities

import solution

input_example = "AOC-2025-Day-05_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-05_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 3),
        pytest.param(input_full, 737),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value

    # Re-test using AI generated solution
    import ai_solution_part_1
    value = ai_solution_part_1.solve_part1(filename)    
    assert expected == value
    

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param([(1, 1), (3, 5)], {(1, 1), (3, 5)}),
        pytest.param([(3, 5), (1, 1)], {(1, 1), (3, 5)}),
        pytest.param([(3, 5), (1, 1), (2,4)], {(1, 1), (2, 5)}),
        pytest.param([(3, 5), (10, 14), (16, 18), (12, 20)], {(3, 5), (10, 20)}),
        pytest.param([(3, 5), (10, 14), (16, 20), (12, 18)], {(3, 5), (10, 20)}),
        pytest.param([(16, 20), (10, 14), (12, 18), (3, 5)], {(3, 5), (10, 20)}), # Unsorted input list
        pytest.param([(16, 20), (10, 14), (12, 18), (10, 14), (3, 5)], {(3, 5), (10, 20)}), # Unsorted input list with duplicates
    ],    
)
def test_merge_overlapping_ranges(input, expected):
    actual = solution.merge_overlapping_ranges(input)
    assert actual == expected


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 14),
        pytest.param(input_full, 357485433193284),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value

    # Re-test using AI generated solution
    import ai_solution_part_2
    value = ai_solution_part_2.solve_part2(filename)
    assert expected == value