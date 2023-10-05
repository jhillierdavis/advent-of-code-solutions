from helpers.fileutils import get_file_first_line_to_int_array
from helpers.fileutils import get_file_lines

def test_get_file_first_line_to_array():
    # When:
    arr = get_file_first_line_to_int_array('fileutils-test-data-array.txt')

    # Then:
    assert arr == [3,4,3,1,2]


def test_get_file_lines():
    # When:
    lines = get_file_lines('fileutils-test-data-multiline.txt')

    # Then:
    assert lines == ['Alpha', 'Beta', 'Gamma']
