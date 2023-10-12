import pytest

# Local
import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 17),
        pytest.param("puzzle-input-full.txt", 682), 
    ],    
)
def test_part1_solution(filename, expected):
    assert solution.process_first_fold_from_filename(filename) == expected