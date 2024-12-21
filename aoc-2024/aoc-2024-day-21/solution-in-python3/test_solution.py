import pytest

import solution

input_example = "AOC-2024-Day-21_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-21_Puzzle-Input-Full.txt"

@pytest.mark.parametrize(
    "code, sequence, expected",
    [
        pytest.param('029A', '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A', 68 * 29),
        pytest.param('980A', '<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A', 60 * 980),
        pytest.param('179A', '<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A', 68 * 179), 
        pytest.param('456A', '<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A', 64 * 456),
        pytest.param('379A', '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A', 64 * 379),
    ],    
)
def test_calculate_complexity(code, sequence, expected):
    value = solution.calculate_complexity(code, sequence)
    assert expected == value


@pytest.mark.parametrize(
    "code, expected",
    [
        pytest.param('029A', ['<A^A>^^AvvvA', '<A^A^>^AvvvA', '<A^A^^>AvvvA']),
    ],    
)
def test_get_shortest_directional_sequence_for_code(code, expected):
    value = solution.get_shortest_directional_sequence_for_code(code)
    assert value in expected


@pytest.mark.parametrize(
    "directions, expected",
    [
        pytest.param('<A^A>^^AvvvA', 'v<<A>>^A<A>AvA<^AA>A<vAAA>^A'),
        pytest.param('v<<A>>^A<A>AvA<^AA>A<vAAA>^A', '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'),
    ],    
)
def test_get_shortest_directional_sequence_for_directions(directions, expected):
    value = solution.get_shortest_directional_sequence_for_directions(directions)
    assert len(value) == len(expected)

@pytest.mark.parametrize(
    "code, expected",
    [
        pytest.param('029A', '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'),
        pytest.param('980A', '<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A'),
        pytest.param('179A', '<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'),
        pytest.param('456A', '<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A'),
        pytest.param('379A', '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'),
    ],    
)
def test_shortest_sequence_of_button_presses(code, expected):
    directions = solution.get_shortest_directional_sequence_for_code(code)
    directions = solution.get_shortest_directional_sequence_for_directions(directions)
    value = solution.get_shortest_directional_sequence_for_directions(directions)
    assert len(value) == len(expected)


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 126384),
        #pytest.param(input_full, -1),
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
