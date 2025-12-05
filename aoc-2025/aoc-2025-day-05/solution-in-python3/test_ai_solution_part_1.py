import pytest
from ai_solution_part_1 import count_integers_in_ranges

@pytest.mark.parametrize(
    "ranges, integers, expected",
    [
        (["3-5", "10-14", "16-20", "12-18"], [1, 5, 8, 11, 17, 32], 3),
        (["1-2", "4-6"], [1, 2, 3, 4, 5, 6], 5),  # 3 is outside
        (["5-10"], [1, 5, 7, 10, 12], 3),         # 5,7,10 inside
        (["2-4", "6-8"], [2, 4, 5, 6, 8], 4),     # 2,4,6,8 inside
        (["1-100"], [50, 101, 0, 99], 2),         # 50,99 inside
        ([], [1,2,3], 0),                         # no ranges
    ]
)
def test_count_integers_in_ranges(ranges, integers, expected):
    assert count_integers_in_ranges(ranges, integers) == expected
