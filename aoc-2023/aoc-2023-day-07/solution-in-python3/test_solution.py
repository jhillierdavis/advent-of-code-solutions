import pytest

import solution


@pytest.mark.parametrize(
    "list_of_hands,expected",
    [
        pytest.param(['33332','2AAAA'], ['2AAAA','33332']), # Both four of a kind
        pytest.param(['2AAAA','33332'], ['2AAAA','33332']), # Both four of a kind
        pytest.param(['77888','77788'], ['77788','77888']), # Both full house
        pytest.param(['77788','77888'], ['77788','77888']), # Both full house
        pytest.param(['AKQJT','AKQTJ'], ['AKQTJ', 'AKQJT']),
        pytest.param(['AKQTJ','AKQJT'], ['AKQTJ','AKQJT']), 
        

        #pytest.param(['AAAAA','AA8AA'], ['AA8AA', 'AAAAA']),
        #pytest.param(['23332','AA8AA'], ['23332','AA8AA' ]),
        #pytest.param(['32T3K','T55J5','KK677' 'KTJJT','QQQJA'], ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']),
    ],    
)
def test_sort_by_rank(list_of_hands, expected):
    assert solution.sort_by_rank(list_of_hands) == expected

"""
@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 6440),
    ],    
)
def test_get_total_winnings(input, expected):
    assert solution.get_total_winnings(input) == expected
"""