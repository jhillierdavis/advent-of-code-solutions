import pytest

@pytest.mark.parametrize(
    "ranges, expected",
    [
        # No ranges
        ([], 0),                                   
        # Basic overlapping
        (["3-5", "4-10"], 8),  # 3–10 inclusive
        (["3-5", "10-14", "16-20", "12-18"], 14),  # Example from prompt
        # Single range
        (["5-10"], 6),
        (["1-5"], 5),
        # Single-value ranges
        (["5-5", "6-6", "7-7"], 3),
        # Touching ranges
        (["1-5", "5-10"], 10),
        (["1-3", "4-6"], 6),  # 1–6 inclusive
        # Disjoint ranges
        (["1-3", "10-12"], 6),
        (["1-3", "5-7"], 6),
        (["10-20", "15-25"], 16),                  # Overlapping ranges        
        (["5-5", "6-6"], 2),                       # Single-value ranges
        # Mixed overlaps
        (["3-5", "10-14", "16-20", "12-18"], 14),
        # Large ranges (ensure no expansion)
        (["100-200"], 101),
        (["1-1000000000"], 1_000_000_000),
        # Empty input
        ([], 0),
        # Reversed ranges
        (["10-5"], 6),  # Should normalize to 5–10
        # Complex merging
        (["1-2", "4-7", "3-3", "10-12", "11-15"], 2 + 4 + 1 + 6),  # 1–2, 3–7, 10–15
    ]
)
def test_count_unique_integers(ranges, expected):
    from ai_solution_part_2 import count_unique_integers
    assert count_unique_integers(ranges) == expected
