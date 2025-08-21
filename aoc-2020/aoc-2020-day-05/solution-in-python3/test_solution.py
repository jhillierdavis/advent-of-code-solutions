import pytest

import solution


@pytest.mark.parametrize(
    "boarding_pass, expected_row, expected_column, expected_seat_id",
    [
        pytest.param('FBFBBFFRLR', 44, 5, 357),
        pytest.param('BFFFBBFRRR', 70, 7, 567),
        pytest.param('FFFBBBFRRR', 14, 7, 119),
        pytest.param('BBFFBBFRLL', 102, 4, 820),        
    ],    
)
def test_get_seat_id(boarding_pass, expected_row, expected_column, expected_seat_id):
    row = solution.get_row(boarding_pass)
    assert expected_row == row

    column = solution.get_column(boarding_pass)
    assert expected_column == column
    
    seat_id = solution.get_seat_id(boarding_pass)
    assert expected_seat_id == seat_id


input_example = "AOC-2020-Day-05_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-05_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 820),
        pytest.param(input_full, 828),
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
