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
    "alpha, beta, expected",
    [
        pytest.param(1,2,12),
        pytest.param(12,345,12345),
        pytest.param(0,9,9),
        pytest.param(9,0,90),
    ],    
)
def test_concatonate(alpha, beta, expected):
    assert expected == numutils.concatonate(alpha, beta)

