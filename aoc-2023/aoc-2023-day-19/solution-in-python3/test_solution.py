import pytest

import solution

@pytest.mark.parametrize(
    "filename,part,expected",
    [
        pytest.param("puzzle-input-example.txt","{x=787,m=2655,a=1222,s=2876}", 'A'),
        pytest.param("puzzle-input-example.txt","{x=1679,m=44,a=2067,s=496}", 'R'),
        pytest.param("puzzle-input-example.txt","{x=2036,m=264,a=79,s=2244}", 'A'),
        pytest.param("puzzle-input-example.txt","{x=2461,m=1339,a=466,s=291}", 'R'),
        pytest.param("puzzle-input-example.txt","{x=2127,m=1623,a=2188,s=1013}", 'A'),        
        #pytest.param("puzzle-input-full.txt", -1),
    ],    
)
def test_workflow_processing_for_part(filename, part, expected):
    workflow_mapping = solution.get_workflow_mappings_from(filename)

    assert solution.workflow_processing_for_part(workflow_mapping, part) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 19114),
        pytest.param("puzzle-input-full.txt", 446517),
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part1(filename) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 167409079868000),
        pytest.param("puzzle-input-full.txt", 130090458884662),
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected