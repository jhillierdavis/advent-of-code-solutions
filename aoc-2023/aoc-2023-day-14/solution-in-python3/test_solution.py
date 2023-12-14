import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example-slid-north.txt", 18),
    ],    
)
def test_count_rounded_rocks_from(filename, expected):
    assert solution.count_rounded_rocks_from(filename) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example-slid-north.txt", 136),
    ],    
)
def test_calculate_load_from(filename, expected):
    assert solution.calculate_load_from(filename) == expected    


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 136),
        #pytest.param("puzzle-input-full.txt", 113456),
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part1(filename) == expected  


@pytest.mark.parametrize(
    "list_of_numbers,expected",
    [
        pytest.param([1,2,3], False),
        pytest.param([1,2,3,1,2,3], True),
        pytest.param([33841, 35099, 34910, 34913, 34817, 34739, 34641, 34474, 34443, 34417, 34416, 34320, 34276, 34180, 34137, 34093, 34059, 33952, 34012, 33931, 33826, 33809, 33733, 33671, 33655, 33564, 33503, 33514, 33478, 33491, 33540, 33414, 33397, 33393, 33318, 33237, 33287, 33280, 33243, 33261, 33283, 33255, 33216, 33215, 33209, 33242, 33235, 33157, 33154, 33121, 33083, 33051, 33045, 32993, 32939, 32918, 32875, 32788, 32833, 32818, 32776, 32771, 32779, 32749, 32719, 32692, 32616, 32613, 32629, 32634, 32625, 32642, 32556, 32509, 32537, 32497, 32491, 32462, 32456, 32423, 32438, 32448, 32475, 32498, 32476, 32509, 32497, 32475, 32495, 32503, 32496, 32500, 32521, 32501, 32506, 32477, 32471, 32495, 32504, 32495, 32513, 32521, 32484, 32500, 32487, 32474, 32489, 32520, 32495, 32496, 32515, 32494, 32503, 32481, 32490, 32489, 32503, 32489, 32506, 32518, 32488, 32519, 32481, 32473, 32483, 32513, 32492, 32500, 32534, 32488, 32502, 32475, 32483, 32486, 32507, 32508, 32500, 32517, 32482, 32512, 32478, 32477, 32502, 32507, 32491, 32494, 32527, 32485, 32506, 32494, 32477, 32485, 32501], True)
    ],    
)
def test_is_repeating_sequence_in(list_of_numbers, expected):
    assert solution.is_repeating_sequence_in(list_of_numbers) == expected



@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 64),
        pytest.param("puzzle-input-full.txt", 0), # < 118755
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part2(filename) == expected