import pytest

import crt

# Ref.: https://en.wikipedia.org/wiki/Chinese_remainder_theorem

@pytest.mark.parametrize(
    "moduli, remainders, expected",
    [
        pytest.param([3, 5, 7], [2, 3, 2], 23),
        pytest.param([67,7,59,61], [0,6,57,58], 754018),
        pytest.param([1789,37,47,1889],[0,36,45,1886], 1202161486),
    ],    
)
def test_get_earliest_sequence_timestamp(moduli, remainders, expected):
    assert crt.chinese_remainder_theorem(remainders, moduli) == expected