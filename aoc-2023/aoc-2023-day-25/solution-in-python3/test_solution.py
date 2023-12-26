import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 54),
        pytest.param("puzzle-input-full.txt", 562978), # > 510120 (as too low!)
    ],    
)
def test_solve(filename, expected):
    #assert solution.solve_using_kargers_algorithm_from(filename) == expected
    assert solution.solve_using_networkx_graph_from(filename) == expected