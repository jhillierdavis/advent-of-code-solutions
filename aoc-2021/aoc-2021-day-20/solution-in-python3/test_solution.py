import pytest

import solution

input_example = "AOC-2021-Day-20_Puzzle-Input-Example.txt"
input_full = "AOC-2021-Day-20_Puzzle-Input-Full.txt"

@pytest.mark.parametrize(
    "filename",
    [
        pytest.param(input_example),
        #pytest.param(input_full),
    ],    
)
def test_image_enhancement_algorithm(filename):
    image_enhancement_algorithm = solution.get_image_enhancement_algorithm(filename)

    assert len(image_enhancement_algorithm) == 512

    assert image_enhancement_algorithm[0] == '.'
    assert image_enhancement_algorithm[10] == '#'
    assert image_enhancement_algorithm[20] == '#'
    assert image_enhancement_algorithm[30] == '#'
    assert image_enhancement_algorithm[34] == '#'
    assert image_enhancement_algorithm[40] == '#'
    assert image_enhancement_algorithm[50] == '#'
    assert image_enhancement_algorithm[60] == '.'
    assert image_enhancement_algorithm[70] == '.'


def test_pixels_to_binary():
    actual = solution.pixels_to_binary("...#...#.")
    assert actual == "000100010"
    assert int(actual, 2) == 34


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 35),
        pytest.param(input_full, -1), #  5708 too high
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, -1),
        #pytest.param(input_full, -1),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
