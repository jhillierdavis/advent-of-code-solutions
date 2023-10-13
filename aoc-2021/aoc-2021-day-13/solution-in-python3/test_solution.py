import pytest

# Local
import solution
import helpers.grid as hg

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 17),
        pytest.param("puzzle-input-full.txt", 682), 
    ],    
)
def test_part1_solution(filename, expected):
    assert solution.process_first_fold_from_filename(filename) == expected


@pytest.mark.parametrize(
    "filename",
    [
        pytest.param("puzzle-input-example.txt"),
        pytest.param("puzzle-input-full.txt"), 
    ],    
)
def test_part1_solution(filename):
    g = solution.process_all_folds_from_filename(filename) 
    print(f"{g}")
    hg.display_grid(g)
    pytest.fail() # TODO