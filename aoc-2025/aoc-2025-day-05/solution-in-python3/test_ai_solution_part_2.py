import pytest

@pytest.mark.parametrize(
    "ranges, expected",
    [
        (["3-5", "10-14", "16-20", "12-18"], 14),  # Example from prompt
        (["1-5"], 5),                              # Single range
        (["1-5", "5-10"], 10),                     # Touching ranges
        (["1-3", "5-7"], 6),                       # Disjoint ranges
        (["10-20", "15-25"], 16),                  # Overlapping ranges
        (["100-200"], 101),                        # Large range
        ([], 0),                                   # No ranges
        (["5-5", "6-6"], 2),                       # Single-value ranges
    ]
)
def test_count_unique_integers(ranges, expected):
    from ai_solution_part_2 import count_unique_integers
    assert count_unique_integers(ranges) == expected
