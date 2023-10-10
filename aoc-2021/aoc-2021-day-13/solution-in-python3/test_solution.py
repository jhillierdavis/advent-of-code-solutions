import pytest

def count_dots():
    return -1 # TODO

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 17),
#        pytest.param("puzzle-input-full.txt", 0), 
    ],    
)
def test_part1_solution(filename, expected):
    assert count_dots() == expected