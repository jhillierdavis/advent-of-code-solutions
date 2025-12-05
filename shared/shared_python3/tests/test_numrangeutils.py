import pytest
import helpers.numrangeutils as numrangeutils


@pytest.mark.parametrize(
    "num, range_list, expected",
    [
        pytest.param(0, [(1, 1), (3, 5)], False),
        pytest.param(0, [(3, 5), (1, 1)], False),
        pytest.param(1, [(1, 1), (3, 5)], True),
        pytest.param(1, [(3, 5), (1, 1)], True),
        pytest.param(2, [(1, 1), (3, 5)], False),
        pytest.param(2, [(3, 5), (1, 1)], False),
        pytest.param(3, [(1, 1), (3, 5)], True),
        pytest.param(4, [(1, 1), (3, 5)], True),
        pytest.param(5, [(1, 1), (3, 5)], True),
        pytest.param(6, [(1, 1), (3, 5)], False),
    ],    
)
def test_is_number_in_range_list(num, range_list, expected):
    actual = numrangeutils.is_number_in_range_list(num, range_list)
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param([(1, 1), (3, 5)], [(1, 1), (3, 5)]),
        pytest.param([(3, 5), (1, 1)], [(1, 1), (3, 5)]),
        pytest.param([(3, 5), (1, 1), (2, 4)], [(1, 1), (2, 4), (3, 5)]),
    ],    
)
def test_get_range_list_sorted_ascending(input, expected):
    # Prepare:
    original = input.copy()
    assert original == input

    # When: the input range list is sorted
    actual = numrangeutils.get_range_list_sorted_ascending(input)

    # Then: the order is ascending
    assert actual == expected

    # And: check that the original list remains unchanged
    assert original == input




@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param([(1, 1), (3, 5)], {(1, 1), (3, 5)}),
        pytest.param([(3, 5), (1, 1)], {(1, 1), (3, 5)}),
        pytest.param([(3, 5), (1, 1), (2, 4)], {(1, 1), (2, 5)}),
        pytest.param([(3, 5), (10, 14), (16, 18), (12, 20)], {(3, 5), (10, 20)}),
        pytest.param([(3, 5), (10, 14), (16, 20), (12, 18)], {(3, 5), (10, 20)}),
        pytest.param([(16, 20), (10, 14), (12, 18), (3, 5)], {(3, 5), (10, 20)}), # Unsorted input list
        pytest.param([(16, 20), (10, 14), (12, 18), (10, 14), (3, 5)], {(3, 5), (10, 20)}), # Unsorted input list with duplicates
        # Further test cases (based on AI generated unit tests)
        pytest.param([(1,5)],{(1,5)}), # Single range
        pytest.param([(1,5), (5,10)], {(1,10)}), # Touching ranges
        pytest.param([(1,3), (5,7)], {(1,3),(5,7)}), # Disjoint ranges
        pytest.param([(10,20), (15,25)], {(10,25)}), # Overlapping ranges
        pytest.param([(100,200)], {(100,200)}), # Large range
        pytest.param([], set()),  # No ranges
        pytest.param([(5,5), (6,6)], {(5,5),(6,6)}), # Single-value ranges
    ],    
)
def test_merge_overlapping_ranges(input, expected):
    actual = numrangeutils.merge_overlapping_ranges(input)
    assert actual == expected
