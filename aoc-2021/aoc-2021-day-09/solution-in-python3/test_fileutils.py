import fileutils

def test_get_file_first_line_to_array():
    # When:
    lines = fileutils.get_file_lines('puzzle-input-example.txt')

    # Then:
    assert lines == ["2199943210","3987894921","9856789892","8767896789","9899965678"]