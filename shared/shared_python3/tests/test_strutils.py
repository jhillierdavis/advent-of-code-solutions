import pytest

from helpers import strutils

def test_sort_alphbeticallly():
    # Given:
    str  = "bca"

    # Then:
    assert strutils.sort_alphabetically(str) == "abc"

def test_has_subset_of_chars():
    assert strutils.has_subset_of_chars("abc", "bde") == False # intersection

    assert strutils.has_subset_of_chars("abc", "bc") == True
    assert strutils.has_subset_of_chars("abcd", "bd") == True

@pytest.mark.parametrize(
    "source, expected",
    [
        pytest.param('abc', {'a':1, 'b':1, 'c':1}),
        pytest.param('hello!', {'h':1, 'l':2, 'e':1, 'o':1, '!':1}),
        pytest.param('Abba', {'A':1, 'b':2, 'a':1}), 
    ],    
)
def test_get_sorted_char_freq_map_from_string(source, expected):
    assert strutils.get_char_freq_map_from_string(source) == expected


@pytest.mark.parametrize(
    "source, target, expected",
    [
        pytest.param('None here!', 'A', 0), 
        pytest.param('AAAAA', 'A', 5),
        pytest.param('aAaAa', 'A', 2),
        pytest.param('someone@somewhere.com', '@', 1), 
    ],    
)
def test_get_char_occurances_in_string(source, target, expected):
    assert strutils.get_char_occurances_in_string(source, target) == expected