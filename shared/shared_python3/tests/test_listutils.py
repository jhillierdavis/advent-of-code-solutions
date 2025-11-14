import pytest

from helpers import listutils


@pytest.mark.parametrize(
    "lst, entry, expected",
    [    
        pytest.param([1,2,3,2,1], 0, -1), # Entry not present
        pytest.param([1,2,3,2,1], 1, 4),
        pytest.param([1,2,3,2,1], 2, 3),
        pytest.param([1,2,3,2,1], 3, 2),
    ],    
)
def test_last_index_of(lst, entry, expected):    
    assert expected == listutils.last_index_of(lst, entry)