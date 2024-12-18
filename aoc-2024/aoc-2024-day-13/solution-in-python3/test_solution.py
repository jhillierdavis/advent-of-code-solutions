import pytest

import solution

input_example = "AOC-2024-Day-13_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-13_Puzzle-Input-Full.txt"


@pytest.mark.parametrize(
    "presses_A, presses_B, expected",
    [
        pytest.param(80, 40, 280),
        pytest.param(38, 86, 200),
    ],    
)
def test_calculate_cost_from_button_presses(presses_A, presses_B, expected):
    value = solution.calculate_cost_from_button_presses(presses_A, presses_B)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 480),
        pytest.param(input_full, 35729), # 32854?
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value

@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "instruction, expected",
    [
        pytest.param((94, 34, 22, 67, 8400, 5400), (80, 40)),
        pytest.param((26, 66, 67, 21, 12748, 12176), (None, None)),
        pytest.param((17, 86, 84, 37, 7870, 6450), (38, 86)),
        pytest.param((69, 23, 27, 71, 18641, 10279), (None, None)),
        pytest.param((94, 34, 22, 67, 10000000008400, 10000000005400), (None, None)),
        pytest.param((26, 66, 67, 21, 10000000012748, 10000000012176), (118679050709, 103199174542)),
        #pytest.param((17, 86, 84, 37, 10000000007870, 10000000006450), (None, None)),
        #pytest.param((69, 23, 27, 71, 10000000018641, 10000000010279), (102851800151, 107526881786)),
    ],    
)
def test_determine_button_presses_speculatively(instruction, expected):
    ax, ay, bx, by, px, py = instruction
    value = solution.determine_buttons_presses_speculatively(ax, ay, bx, by, px, py)    
    assert expected == value    


@pytest.mark.parametrize(
    "instruction, expected",
    [
        pytest.param((94, 34, 22, 67, 8400, 5400), (80, 40)),
        pytest.param((26, 66, 67, 21, 12748, 12176), (None, None)),
        pytest.param((17, 86, 84, 37, 7870, 6450), (38, 86)),
        pytest.param((69, 23, 27, 71, 18641, 10279), (None, None)),
        pytest.param((94, 34, 22, 67, 10000000008400, 10000000005400), (None, None)),
        pytest.param((26, 66, 67, 21, 10000000012748, 10000000012176), (118679050709, 103199174542)),
        pytest.param((17, 86, 84, 37, 10000000007870, 10000000006450), (None, None)),
        pytest.param((69, 23, 27, 71, 10000000018641, 10000000010279), (102851800151, 107526881786)),
    ],    
)
def test_determine_button_presses(instruction, expected):
    ax, ay, bx, by, px, py = instruction
    value = solution.determine_buttons_presses(ax, ay, bx, by, px, py)    
    assert expected == value



#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, prize_offset, expected",
    [
        pytest.param(input_example, 0, 480),
        pytest.param(input_full, 0, 35729),
        pytest.param(input_example, 10000000000000, 875318608908),
        pytest.param(input_full, 10000000000000, 88584689879723), # Too high: 90988267260208
    ],    
)
def test_solve_part2(filename, prize_offset, expected):
    value = solution.solve_part2(filename, prize_offset)    
    assert expected == value