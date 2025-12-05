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
    # Test inital manually crafted solution
    value = solution.solve_part1(filename)    
    assert expected == value

    # Re-test using subsequent AI (LLM) generated solution
    import ai_solution_part_1
    value = ai_solution_part_1.solve_part1(filename)    
    assert expected == value
    

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 14),
        pytest.param(input_full, 357485433193284),
    ],    
)
def test_solve_part2(filename, expected):
    # Test inital manually crafted solution
    value = solution.solve_part2(filename)    
    assert expected == value

    # Re-test using subsequent AI (LLM) generated solution
    import ai_solution_part_2
    value = ai_solution_part_2.solve_part2(filename)
    assert expected == value