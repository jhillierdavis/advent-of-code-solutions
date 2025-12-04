import pytest

# Unit tests for manual & (subsequently) AI (CoPilot) generated (core algorithm) solutions.
# Re-solved (using AI) to refine prompting skill & explore current AI caperbilities
import solution, ai_solution_part_1, ai_solution_part_2 

input_example = "AOC-2025-Day-04_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-04_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 13),
        pytest.param(input_full, 1551),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value

    # Retry using AI solution
    input = ai_solution_part_1.read_file_as_string(filename)
    value = ai_solution_part_1.solve_from_text(input)
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 43),
        pytest.param(input_full, 9784),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value

    # Retry using AI solution
    input = ai_solution_part_1.read_file_as_string(filename)
    value = ai_solution_part_2.iterative_replace(input)
    assert expected == value   