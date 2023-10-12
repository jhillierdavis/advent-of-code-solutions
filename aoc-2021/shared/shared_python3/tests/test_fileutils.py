from helpers.fileutils import get_file_first_line_to_int_array
from helpers.fileutils import get_file_lines
from helpers.fileutils import  get_lines_before_empty_from_file
from helpers.fileutils import  get_lines_after_empty_from_file

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


def test_get_lines_before_empty_from_file():
    # When:
    lines = get_lines_before_empty_from_file('fileutils-test-data-mixed.txt')

#    for l in lines:
#        print(f"DEBUG: line: {l}")

    # Then:
    assert len(lines) == 17 
    assert "6,12" in lines


def test_get_lines_after_empty_from_file():
    # When:
    lines = get_lines_after_empty_from_file('fileutils-test-data-mixed.txt')

#    for l in lines:
#        print(f"DEBUG: line: {l}")

    # Then:
    assert len(lines) == 2 
    assert "fold along y=7" in lines    
