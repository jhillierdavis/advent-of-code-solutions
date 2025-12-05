import pytest
import helpers.numrangeutils as numrangeutils

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param([(1, 1), (3, 5)], {(1, 1), (3, 5)}),
        pytest.param([(3, 5), (1, 1)], {(1, 1), (3, 5)}),
        pytest.param([(3, 5), (1, 1), (2,4)], {(1, 1), (2, 5)}),
        pytest.param([(3, 5), (10, 14), (16, 18), (12, 20)], {(3, 5), (10, 20)}),
        pytest.param([(3, 5), (10, 14), (16, 20), (12, 18)], {(3, 5), (10, 20)}),
        pytest.param([(16, 20), (10, 14), (12, 18), (3, 5)], {(3, 5), (10, 20)}), # Unsorted input list
        pytest.param([(16, 20), (10, 14), (12, 18), (10, 14), (3, 5)], {(3, 5), (10, 20)}), # Unsorted input list with duplicates
    ],    
)
def test_merge_overlapping_ranges(input, expected):
    actual = numrangeutils.merge_overlapping_ranges(input)
    assert actual == expected
