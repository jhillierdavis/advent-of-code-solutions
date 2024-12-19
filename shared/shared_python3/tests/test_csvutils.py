import pytest

from helpers import csvutils

@pytest.mark.parametrize(
    "input, expected",
    [         
        pytest.param('a, b, c', ['a','b','c']), 
        pytest.param('a,b,c', ['a','b','c']), 
        pytest.param('a,b , c', ['a','b','c']), 
        pytest.param('a,    b,c', ['a','b','c']), 
        pytest.param('a b c', ['a b c']),
        pytest.param('solo', ['solo']),
        pytest.param('left, right', ['left', 'right']),
        pytest.param('', []),
    ],    
)
def test_comma_separated_values_to_list(input:str, expected) -> list:
    assert csvutils.comma_separated_values_to_list(input) == expected
