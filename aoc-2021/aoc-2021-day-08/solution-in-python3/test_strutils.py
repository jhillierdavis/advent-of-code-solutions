import strutils

def test_sort_alphbeticallly():
    # Given:
    str  = "bca"

    # Then:
    assert strutils.sort_alphabetically(str) == "abc"

def test_has_subset_of_chars():
    assert strutils.has_subset_of_chars("abc", "bde") == False # intersection

    assert strutils.has_subset_of_chars("abc", "bc") == True
    assert strutils.has_subset_of_chars("abcd", "bd") == True
