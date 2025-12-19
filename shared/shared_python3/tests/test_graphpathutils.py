import pytest

import helpers.graphpathutils

graph_a_to_g = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": ["G"],
        "E": ["G"],
        "F": ["G"],
        "G": []
    }

graph_aoc_2025_day_11 = {'aaa': ['you', 'hhh'], 'you': ['bbb', 'ccc'], 'bbb': ['ddd', 'eee'], 'ccc': ['ddd', 'eee', 'fff'], 'ddd': ['ggg'], 'eee': ['out'], 'fff': ['out'], 'ggg': ['out'], 'hhh': ['ccc', 'fff', 'iii'], 'iii': ['out']}

@pytest.mark.parametrize(
    "graph, start, stop, expected",
    [
        pytest.param(graph_a_to_g, 'A', 'F', 1), # A->C->F
        pytest.param(graph_a_to_g, 'A', 'G', 3), # A->B->D->G , A->B->E-G , A->C->F-G 
        pytest.param(graph_a_to_g, 'A', 'Z', 0), # No Z
        pytest.param(graph_a_to_g, 'X', 'Z', 0), # No X or Z
        pytest.param(graph_aoc_2025_day_11, 'you', 'out', 5),
    ],    
)
def test_find_path_count(graph, start, stop, expected):
    # When:
    num = helpers.graphpathutils.find_path_count(graph, start, stop)

    # Then:
    assert expected == num