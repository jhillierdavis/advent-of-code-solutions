import pytest

import solution

input_example = "AOC-2024-Day-09_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-09_Puzzle-Input-Full.txt"

@pytest.mark.parametrize(
    "diskmap, expected",
    [
        pytest.param('12345', '0..111....22222'),
        pytest.param('2333133121414131402', '00...111...2...333.44.5555.6666.777.888899'),
    ],    
)
def test_to_block_representation_from(diskmap, expected):
    q = solution.to_block_representation_from(diskmap)
    assert expected ==  solution.queue_to_string(q)

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "diskmap, block_representation, expected",
    [
        #pytest.param('12345', '0..111....22222', '022111222......'),
        #pytest.param('00...111...2...333.44.5555.6666.777.888899', '00...111...2...333.44.5555.6666.777.888899', '0099811188827773336446555566..............'),
        pytest.param('12345', '0..111....22222', '022111222'),
        pytest.param('2333133121414131402', '00...111...2...333.44.5555.6666.777.888899', '0099811188827773336446555566'),
    ],    
)
def test_to_compacted_from(diskmap, block_representation, expected):
    q = solution.to_block_representation_from(diskmap)
    #print(f"DEBUG: q={q}")
    assert block_representation == solution.queue_to_string(q)
    #print(f"DEBUG: q={q}")

    q_compacted = solution.to_compacted_from(q)
    assert expected == solution.queue_to_string(q_compacted)


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "compacted, expected",
    [
        pytest.param('0099811188827773336446555566..............', 1928),
    ],    
)
def test_to_checksum_from(compacted, expected):
    checksum = solution.to_checksum_from(compacted)
    assert expected == checksum


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 1928), 
        pytest.param(input_full, 6288599492129), # 89514618001 too low!
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 2858),
        #pytest.param(input_full, "TODO"),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value
