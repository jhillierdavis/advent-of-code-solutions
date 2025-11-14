import pytest

import helpers.numutils as numutils


@pytest.mark.parametrize(
    "number, expected",
    [    
        pytest.param(0, True),
        pytest.param(1, False),
        pytest.param(-1, False),
        pytest.param(2, True),
        pytest.param(-2, True),
        pytest.param(3, False),
        pytest.param(4, True),
        pytest.param(99, False),
        pytest.param(100, True),
    ],    
)
def test_is_even(number, expected):    
    assert expected == numutils.is_even(number)


@pytest.mark.parametrize(
    "number, expected",
    [    
        pytest.param(0, False),
        pytest.param(1, True),
        pytest.param(-1, True),
        pytest.param(2, False),
        pytest.param(-2, False),
        pytest.param(3, True),
        pytest.param(4, False),
        pytest.param(99, True),
        pytest.param(100, False),
    ],    
)
def test_is_odd(number, expected):    
    assert expected == numutils.is_odd(number)    


@pytest.mark.parametrize(
    "left, right, expected",
    [
        pytest.param(1,2,12),
        pytest.param(12,345,12345),
        pytest.param(0,9,9),
        pytest.param(9,0,90),
    ],    
)
def test_concatonate(left, right, expected):
    assert expected == numutils.concatonate(left, right)


@pytest.mark.parametrize(
    "array_of_integers, expected",
    [
        pytest.param([75,47,61,53,29], 61),
        pytest.param([97,61,53,29,13], 53),
        pytest.param([75,29,13], 29),
        pytest.param([1,2,3,4], 2), # Even length
        pytest.param([], None),
    ],    
)
def test_get_middle_value_from(array_of_integers, expected):
    # When:
    value = numutils.get_middle_value_from(array_of_integers)   

    # Then:
    assert expected == value


@pytest.mark.parametrize(
    "value, min, max, expected",
    [
        pytest.param(5, 1, 10, True),
        pytest.param(0, 1, 10, False),
        pytest.param(10, 1, 10, True),
    ],    
)
def test_is_within_range(value, min, max, expected):
    value = numutils.is_within_range(value, min, max)    
    assert expected == value
