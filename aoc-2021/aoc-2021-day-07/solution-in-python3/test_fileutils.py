import fileutils

def test_get_file_first_line_to_array():
    # When:
    arr = fileutils.get_file_first_line_to_int_array('puzzle-input-sample.txt')

    # Then:
    assert arr == [16,1,2,0,4,2,7,1,2,14]