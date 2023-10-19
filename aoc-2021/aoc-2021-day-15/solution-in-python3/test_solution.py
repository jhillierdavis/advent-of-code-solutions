import pytest

# Local
import solution, dijkstras_algorithm_solution

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
    ],    
)
def test_solution(filename, expected):
    assert dijkstras_algorithm_solution.calcuate_lowest_risk_score(filename) == expected