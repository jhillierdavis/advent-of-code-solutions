import pytest

import solution

@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False), 
        pytest.param('12345', False), 
        pytest.param('33332', True), 
        pytest.param('2AAAA', True), 
        pytest.param('QQ5QQ', True), 
    ],    
)
def test_is_four_of_a_kind(hand, expected):
    assert solution.is_four_of_a_kind(hand) == expected

@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False), 
        pytest.param('12345', False), 
        pytest.param('AAAAA', True),
        pytest.param('11111', True), 
        pytest.param('TTTTT', True), 
    ],    
)
def test_is_five_of_a_kind(hand, expected):
    assert solution.is_five_of_a_kind(hand) == expected


@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False),         
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False),
        pytest.param('12345', False), 
        pytest.param('23456', False),
        pytest.param('1QA98', False),
        pytest.param('23332', True),
        pytest.param('TTT98', False),
        pytest.param('23332', True),
    ],    
)
def test_is_full_house(hand, expected):
    assert solution.is_full_house(hand) == expected    


@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False),         
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False),
        pytest.param('12345', False), 
        pytest.param('23456', False),
        pytest.param('1QA98', False),
        pytest.param('23332', False),
        pytest.param('TTT98', True),        
    ],    
)
def test_three_of_a_kind(hand, expected):
    assert solution.is_three_of_a_kind(hand) == expected    

@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False),         
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False),
        pytest.param('12345', False), 
        pytest.param('23456', False),
        pytest.param('1QA98', False),
        pytest.param('A23A4', False), # One pair
        pytest.param('23432', True), # Two pair
    ],    
)
def test_is_two_pair(hand, expected):
    assert solution.is_two_pair(hand) == expected


@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False),         
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False),
        pytest.param('12345', False), 
        pytest.param('23456', False),
        pytest.param('1QA98', False),
        pytest.param('23432', False), # Two pair
        pytest.param('A23A4', True), # One pair

    ],    
)
def test_is_one_pair(hand, expected):
    assert solution.is_one_pair(hand) == expected

@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False),         
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False),
        pytest.param('12345', True), 
        pytest.param('23456', True),
        pytest.param('1QA98', True),
    ],    
)
def test_is_distinct(hand, expected):
    assert solution.is_distinct(hand) == expected


@pytest.mark.parametrize(
    "list_of_hands,expected",
    [
        pytest.param(['33332','2AAAA'], ['2AAAA','33332']), # Both four of a kind
        pytest.param(['2AAAA','33332'], ['2AAAA','33332']), # Both four of a kind
        pytest.param(['77888','77788'], ['77788','77888']), # Both full house
        pytest.param(['77788','77888'], ['77788','77888']), # Both full house
        pytest.param(['AKQJT','AKQTJ'], ['AKQTJ', 'AKQJT']),
        pytest.param(['AKQTJ','AKQJT'], ['AKQTJ','AKQJT']), 
        pytest.param(['AAAAA','AA8AA'], ['AA8AA', 'AAAAA']),
        pytest.param(['23332','AA8AA'], ['23332','AA8AA' ]),
        pytest.param(['32T3K','T55J5','KK677','KTJJT','QQQJA'], ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']),
    ],    
)
def test_sort_by_rank(list_of_hands, expected):
    assert solution.sort_by_rank(list_of_hands) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 6440),
        pytest.param('puzzle-input-full.txt', 248217452),
    ],    
)
def test_get_total_winnings(input, expected):
    assert solution.get_total_winnings(input) == expected

import solution_part2

@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False), 
        pytest.param('12345', False),
        pytest.param('J1112', False),
        pytest.param('JJAA1', False), 
        pytest.param('JJJA1', False),
        pytest.param('JJJAB', False),
        pytest.param('AAAAA', True),        
        pytest.param('11111', True), 
        pytest.param('TTTTT', True),         
        pytest.param('JAAAA', True),
        pytest.param('JJAAA', True), 
        pytest.param('JJJAA', True),
        pytest.param('JJJJA', True),
        pytest.param('JJJJJ', True),
    ],    
)
def test_is_five_of_a_kind_with_wildcard_jokers(hand, expected):
    assert solution_part2.is_five_of_a_kind(hand) == expected


@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('AAAAA', True),
        pytest.param('11111', True), 
        pytest.param('TTTTT', True), 
        pytest.param('12345', False),        
        pytest.param('JAAB1', False),        
        pytest.param('JJAB1', False),
        pytest.param('J123J', False), 
        pytest.param('J1123', False),
        pytest.param('J1122', False), 
        pytest.param('AA8AA', True),
        pytest.param('33332', True), 
        pytest.param('2AAAA', True), 
        pytest.param('QQ5QQ', True), 
        pytest.param('JAAAB', True),
        pytest.param('JJAAB', True), 
        pytest.param('JJJAB', True),
        pytest.param('JJJJB', True),
        pytest.param('QJJQ2', True),
        pytest.param('T55J5', True),
        pytest.param('JAAA1', True),
        pytest.param('JJAA1', True),
        pytest.param('JJJA1', True),
        pytest.param('JJJJ1', True),
        pytest.param('122JJ', True),
        pytest.param('KTJJT', True),
        pytest.param('QQQJA', True),
        pytest.param('J1112', True),
        pytest.param('JJ112', True),
        pytest.param('JJJ12', True),
        pytest.param('JJJJ2', True),
        pytest.param('JJJJJ', True),
    ],    
)
def test_is_four_of_a_kind_with_wildcard_jokers(hand, expected):
    assert solution_part2.is_four_of_a_kind(hand) == expected

@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False),         
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False),
        pytest.param('12345', False), 
        pytest.param('23456', False),
        pytest.param('1QA98', False),
        pytest.param('TTT98', False),
        pytest.param('11223', False),
        pytest.param('J1234', False),
        pytest.param('JJA12', False),
        pytest.param('J1111', False),
        pytest.param('J1234', False),  
        pytest.param('JJ234', False),          
        pytest.param('23332', True),        
        pytest.param('A3A3A', True),
        pytest.param('11122', True),
        pytest.param('JAA22', True),         
        pytest.param('JJ1AA', True),
        pytest.param('JJJ12', True),
        pytest.param('JJJAA', True),
        pytest.param('JJ111', True),
        pytest.param('J1112', True),
        pytest.param('JJ112', True),
        pytest.param('JJJ12', True),
        pytest.param('JJJJ2', True), 
        pytest.param('JJJJJ', True),
        pytest.param('J1222', True),        
        pytest.param('11J22', True),        
        pytest.param('J1J22', True),
        pytest.param('JJ222', True),        
        pytest.param('11JJ2', True),
        pytest.param('JJJ22', True),
        pytest.param('J1JJ2', True),        
        pytest.param('11JJJ', True),
        pytest.param('1JJJJ', True),        
        pytest.param('JJJJJ', True),        
    ],    
)
def test_is_full_house_with_wildcard_jokers(hand, expected):
    assert solution_part2.is_full_house(hand) == expected    


@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False),         
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False),
        pytest.param('12345', False), 
        pytest.param('23456', False),
        pytest.param('1QA98', False),
        pytest.param('23332', False),
        pytest.param('J1234', False), 
        pytest.param('TTT98', True),
        pytest.param('J1123', True), 
        pytest.param('JJ123', True), 
        pytest.param('JJJ12', True),
        pytest.param('JJJJ2', True),
        pytest.param('JJJJJ', True),       
    ],    
)
def test_three_of_a_kind_with_wildcard_jokers(hand, expected):
    assert solution_part2.is_three_of_a_kind(hand) == expected    

@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False),         
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False),
        pytest.param('12345', False), 
        pytest.param('23456', False),
        pytest.param('1QA98', False),
        pytest.param('J1234', False),
        pytest.param('J1111', False),        
        pytest.param('J1234', False),
        pytest.param('J1111', False), # One pair
        pytest.param('A23A4', False), # One pair
        pytest.param('94J8A', False),
        pytest.param('KJ524', False),
        pytest.param('J1112', False),        
        pytest.param('23432', True), # Two pair        
        pytest.param('JJ123', True),
        pytest.param('J3432', True),
        pytest.param('J343J', True),         
        pytest.param('JJ432', True),
        pytest.param('JJJ12', True),
        pytest.param('JJJJ2', True), 
        pytest.param('JJJJJ', True), 
        pytest.param('KK677', True),                
    ],    
)
def test_is_two_pair_with_wildcard_jokers(hand, expected):
    assert solution_part2.is_two_pair(hand) == expected


@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False),         
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False),
        pytest.param('12345', False), 
        pytest.param('23456', False),
        pytest.param('1QA98', False),
        pytest.param('23432', False), # Two pair
        pytest.param('A23A4', True), # One pair
        pytest.param('J1234', True), # One pair
        pytest.param('J23A4', True), # One pair
        pytest.param('JJ3A4', True), # One pair
        pytest.param('J1234', True),
        pytest.param('JJ123', True),
        pytest.param('JJJ12', True),
        pytest.param('JJJJ1', True),
        pytest.param('JJJJJ', True),
        pytest.param('94J8A', True),
        pytest.param('KJ524', True),
    ],    
)
def test_is_one_pair_with_wildcard_jokers(hand, expected):
    assert solution_part2.is_one_pair(hand) == expected


@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('33332', False), 
        pytest.param('2AAAA', False),         
        pytest.param('AAAAA', False),
        pytest.param('11111', False), 
        pytest.param('TTTTT', False),
        pytest.param('11234', False),
        pytest.param('11123', False),
        pytest.param('11112', False),
        pytest.param('11111', False),
        pytest.param('12345', True), 
        pytest.param('23456', True),
        pytest.param('1QA98', True),
        pytest.param('J1234', True),
        pytest.param('JJ123', True),
        pytest.param('JJJ12', True),
        pytest.param('JJJJ1', True),
        pytest.param('JJJJJ', True),
    ],    
)
def test_is_distinct_with_wildcard_jokers(hand, expected):
    assert solution_part2.is_distinct(hand) == expected


@pytest.mark.parametrize(
    "list_of_hands,expected",
    [
        pytest.param(['33332','2AAAA'], ['2AAAA','33332']), # Both four of a kind
        pytest.param(['2AAAA','33332'], ['2AAAA','33332']), # Both four of a kind
        pytest.param(['77888','77788'], ['77788','77888']), # Both full house
        pytest.param(['77788','77888'], ['77788','77888']), # Both full house
        pytest.param(['AAAAA','AA8AA'], ['AA8AA', 'AAAAA']),
        pytest.param(['23332','AA8AA'], ['23332','AA8AA' ]),
        pytest.param(['32T3K','T55J5','KK677','KTJJT','QQQJA'], ['32T3K', 'KK677', 'T55J5', 'QQQJA', 'KTJJT']),
        pytest.param(['T55J5', 'KTJJT', 'QQQJA'], ['T55J5', 'QQQJA', 'KTJJT'])
    ],    
)
def test_sort_by_rank_with_wildcard_jokers(list_of_hands, expected):
    assert solution_part2.sort_by_rank_with_wildcard_jokers(list_of_hands) == expected


@pytest.mark.parametrize(
    "hand,expected",
    [
        pytest.param('JTTTT', 0),
        pytest.param('JJJJJ', 0), 
        pytest.param('588J8', 1),
        pytest.param('J6999', 1),
        pytest.param('588J8', 1),
        pytest.param('J6999', 1),
        pytest.param('6J546', 3),
        pytest.param('KJ524', 5),
        pytest.param('94J8A', 5),
    ],    
)
def test_check_hand_type(hand, expected):
    assert solution_part2.get_hand_type(hand) == expected

# Check part 2 answers
@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 5905),
        pytest.param('puzzle-input-full.txt', 245576185),
    ],    
)
def test_get_total_winnings_with_wildcard_jokers(input, expected):
    assert solution_part2.get_total_winnings_with_wildcard_jokers(input) == expected