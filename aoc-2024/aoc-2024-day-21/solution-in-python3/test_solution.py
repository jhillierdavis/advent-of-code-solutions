import pytest

import solution

input_example = "AOC-2024-Day-21_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-21_Puzzle-Input-Full.txt"

#@pytest.mark.skip
@pytest.mark.parametrize(
    "start, end, expected",
    [
        pytest.param('2', '9', [['^', '^', '>'], ['^', '>', '^'], ['>', '^', '^']]),
    ],    
)
def test_get_shortest_possibilities(start, end, expected):
    g = solution.create_numerical_keypad_grid()

    values = solution.get_shortest_possibilities(g, start, end)
    for v in values:
        assert v in expected
    

#@pytest.mark.skip
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


#@pytest.mark.skip
@pytest.mark.parametrize(
    "code, expected",
    [
        pytest.param('029A', ['<A^A>^^AvvvA', '<A^A^>^AvvvA', '<A^A^^>AvvvA']),
        pytest.param('379A', ['^A^^<<A>>AvvvA', '^A^<^<A>>AvvvA', '^A^<<^A>>AvvvA', '^A<^^<A>>AvvvA', '^A<^<^A>>AvvvA', '^A<<^^A>>AvvvA']),
    ],    
)
def test_get_all_shortest_directional_sequences_for_code(code, expected):
    # Given:
    g_numpad = solution.create_numerical_keypad_grid()

    # When:
    value = solution.get_all_shortest_directional_sequences_for_code(g_numpad, code)

    # Then:
    for v in value:
        assert v in expected
    assert len(value) == len(expected)


@pytest.mark.skip
@pytest.mark.parametrize(
    "directions, expected",
    [
        pytest.param('<A^A>^^AvvvA', 'v<<A>>^A<A>AvA<^AA>A<vAAA>^A'),
        pytest.param('v<<A>>^A<A>AvA<^AA>A<vAAA>^A', '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'),
        pytest.param('^A^^<<A>>AvvvA', '<A>A<AAv<AA^>>AvAA^Av<AAA^>A'), # TODO: Check!
    ],    
)
def test_get_shortest_directional_sequence_for_directions(directions, expected):
    # When:
    value = solution.get_shortest_directional_sequence_for_directions(directions)
    #print(f"DEBUG: directions={directions} value={value}")

    # THen:
    assert len(value) == len(expected)



#@pytest.mark.skip
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 126384),
        #pytest.param(input_full, 212488), # 223804 too high
        #pytest.param(input_example, 3, "TODO"), # Solution Part 1 approach too slow!
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value

import solution_part2

@pytest.mark.parametrize(
    "code, robots, expected",
    [
        pytest.param('029A', 1, 12),
        pytest.param('029A', 2, 28),
        pytest.param('029A', 3, 68),
        pytest.param('029A', 25, 32983284966),
        pytest.param('980A', 3, 60),
        pytest.param('179A', 3, 68),
        pytest.param('980A', 25, 29040553204),
        pytest.param('179A', 25, 32662085210),
        pytest.param('456A', 3, 64),
        pytest.param('456A', 25, 32475283854),
        pytest.param('379A', 3, 64),
        pytest.param('379A', 25, 31349424798),       
    ],    
)
def test_calculate_min_moves_for_code(code, robots, expected):
    min_moves = solution_part2.calculate_min_moves_for_code(code, robots)
    assert expected == min_moves


#@pytest.mark.skip
@pytest.mark.parametrize(
    "filename, intermediaries, expected",
    [
        pytest.param(input_example, 1, 25392),
        pytest.param(input_full, 1, 40774),
        pytest.param(input_example, 2, 53772),
        pytest.param(input_example, 3, 126384),
        pytest.param(input_full, 2, 89986),
        pytest.param(input_full, 3, 212488),
        pytest.param(input_example, 3, 126384),
        pytest.param(input_example, 26, 154115708116294),
        pytest.param(input_full, 26, 258263972600402),
    ],    
)
def test_solve_part2(filename, intermediaries, expected):
    value = solution_part2.solve_part2(filename, intermediaries)
    assert expected == value
