import pytest

# Local
from helpers import validation

@pytest.mark.parametrize(
    "value,expected",
    [
        pytest.param("A string!", True),
        pytest.param("The quick brown fox jumped over the lazy dog!", True),
        pytest.param(None, False),
        pytest.param(12345, False),
        pytest.param(0.5, False),
        pytest.param("", False),
        pytest.param(" ", False),
    ],    
)

def test_is_valid_non_empty_string(value, expected):
    assert validation.is_valid_non_empty_string(value) == expected

@pytest.mark.parametrize(
    "value,expected",
    [
        pytest.param(1, True),
        pytest.param(99, True),
        pytest.param(0, False),
        pytest.param(-1, False),
        pytest.param(None, False),
        pytest.param("A String", False),
        pytest.param(0.5, False),
    ],    
)

def test_is_valid_positve_non_zero_int_value(value, expected):
    assert validation.is_valid_positve_non_zero_int_value(value) == expected