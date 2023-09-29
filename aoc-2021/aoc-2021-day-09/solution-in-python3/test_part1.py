import part1 as solution

def test_part1():
    # When: Solved with example puzzle data
    assert solution.sum_low_points_from_file("puzzle-input-example.txt") == 15

    # Then: Also solved with full puzzle data
    assert solution.sum_low_points_from_file("puzzle-input-full.txt") == 558