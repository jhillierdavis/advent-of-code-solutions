import pytest

import solution

input_example = "AOC-2025-Day-11_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-11_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 5),
        pytest.param(input_full, 699),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)   
    assert expected == value

    # Re-solve using part 2 approach (caching)
    num = solution.solve_part1_using_part2_approach(filename)
    assert expected == num


input_example_part_2 = "AOC-2025-Day-11_Puzzle-Input-Example-Part-2.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_part_2, 2),
        pytest.param(input_full, 388893655378800), # not 791848918299150, not 32932516744905217
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value


@pytest.mark.parametrize(
    "filename, start, stop, expected",
    [
        pytest.param(input_example, 'you', 'out', 5),        
        pytest.param(input_full, 'you', 'out', 699),
        pytest.param(input_example_part_2, 'you', 'out', 0),
        pytest.param(input_example_part_2, 'svr', 'out', 8),
        pytest.param(input_example_part_2, 'svr', 'dac', 2),
        pytest.param(input_example_part_2, 'svr', 'fft', 1),
        pytest.param(input_example_part_2, 'fft', 'dac', 1),
        pytest.param(input_example_part_2, 'dac', 'fft', 0),
        pytest.param(input_example_part_2, 'dac', 'out', 2),
        pytest.param(input_example_part_2, 'fft', 'out', 4),
        pytest.param(input_full, 'svr', 'out', 269728341652862491),
        pytest.param(input_full, 'svr', 'dac', 3041933305555),
        pytest.param(input_full, 'svr', 'fft', 4275),
        pytest.param(input_full, 'fft', 'dac', 17109136),
        pytest.param(input_full, 'dac', 'fft', 0),
        pytest.param(input_full, 'dac', 'out', 5317),
        pytest.param(input_full, 'fft', 'out', 1517071963739),
    ],    
)
def test_find_path_count(filename, start, stop, expected):
    # Given: a graph
    path_map = solution.get_path_map_from_from_file(filename)

    # Then: count distinct paths from start to stop
    num = solution.find_path_count(path_map, start, stop)    
    assert expected == num
