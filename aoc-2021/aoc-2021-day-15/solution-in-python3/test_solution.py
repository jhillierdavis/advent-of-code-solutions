import pytest

# Local
import solution, dijkstras_algorithm_solution, procedural_generation_solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 44),
        pytest.param("puzzle-input-full.txt", 879),
    ],    
)
def test_calculate_initial_path_score(filename, expected):
    assert solution.calculate_initial_path_score_from_file(filename) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 40),
        pytest.param("puzzle-input-jhd-example.txt", 13),
        pytest.param("puzzle-input-full.txt", 696), 
        pytest.param("puzzle-input-example-part2.txt", 315), # Part 2 larger grid (x5) 
    ],    
)
def test_solution(filename, expected):
    assert dijkstras_algorithm_solution.calcuate_lowest_risk_score(filename) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", "puzzle-input-example-part2.txt"),
    ],    
)
def test_procedurally_generated_grid(filename, expected):
    # Given: original & expected grids
    original_grid = dijkstras_algorithm_solution.create_chiton_grid_from_file(filename)
    expected_grid = dijkstras_algorithm_solution.create_chiton_grid_from_file(expected)

    # When: a new grid is generated (based on the original)
    procedurally_generated_grid = procedural_generation_solution.spawn_grid_from(original_grid)

    # Then: the expected (larger) grid is generated
    assert procedurally_generated_grid == expected_grid