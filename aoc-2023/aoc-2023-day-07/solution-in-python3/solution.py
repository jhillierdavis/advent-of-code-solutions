from functools import cmp_to_key
from collections import defaultdict

from helpers import fileutils

def check_char_freq(hand):
    freq = {}
    for c in set(hand):
       freq[c] = hand.count(c)
    return sorted(freq.values(), reverse=True)

def get_max_same_card(hand):
    max_same = 0
    for i in range(len(hand)):
        same = 0
        for j in range(len(hand)):
            if hand[i] == hand[j]:
                same += 1
        if same > max_same:
            max_same = same
    return max_same

def is_five_of_a_kind(hand):
    return get_max_same_card(hand) == 5

def is_four_of_a_kind(hand):
    return get_max_same_card(hand) == 4

def is_full_house(hand):
    freq = check_char_freq(hand)
    #print(f"DEBUG: {freq}")
    return freq == [3,2]

def is_three_of_a_kind(hand):
    freq = check_char_freq(hand)
    #print(f"DEBUG: {freq}")
    return freq == [3,1,1]

def is_two_pair(hand):
    freq = check_char_freq(hand)
    #print(f"DEBUG: {freq}")
    return freq == [2,2,1]

def is_one_pair(hand):
    freq = check_char_freq(hand)
    #print(f"DEBUG: {freq}")
    return freq == [2,1,1,1]

def is_distinct(hand):
    return get_max_same_card(hand) == 1



def get_hand_type(hand):
    #Five of a kind, where all five cards have the same label: AAAAA
    #Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    #Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    #Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    #Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    #One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    #High card, where all cards' labels are distinct: 23456

    if is_five_of_a_kind(hand):
        return 0

    if is_four_of_a_kind(hand):
        return 1

    if is_full_house(hand):
        return 2

    if is_three_of_a_kind(hand):
        return 3

    if is_two_pair(hand):
        return 4

    if is_one_pair(hand):
        return 5

    if is_distinct(hand): # High card
        return 6
        
    raise ValueError(f"Unhanded type for hand={hand}")



def get_card_value(label):
    if label.isnumeric():
        return int(label)

    if label == 'A':
        return 14
    if label == 'K':
        return 13
    if label == 'Q':
        return 12
    if label == 'J':
        return 11
    if label == 'T':
        return 10
    
    raise ValueError("label={label}")
    

def compare_same_hand_type(hand_left, hand_right):
    # A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. 
    # The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

    for i in range(len(hand_left)):
        if not hand_left[i] == hand_right[i]:
            return get_card_value(hand_left[i]) - get_card_value(hand_right[i])
    return 0

def compare(hand_left, hand_right):
    # return a negative value (< 0) when the left item should be sorted before the right item
    # return a positive value (> 0) when the left item should be sorted after the right item
    # return 0 when both the left and the right item have the same weight and should be ordered "equally" without precedence

    if hand_left == hand_right:
        return 0
    
    type_hand_left = get_hand_type(hand_left)
    type_hand_right = get_hand_type(hand_right)

    if not type_hand_left == type_hand_right:
        return  type_hand_right - type_hand_left
    
    return compare_same_hand_type(hand_left, hand_right)


def sort_by_rank(list_of_hands):

    #return ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']
    sorted_list = sorted(list_of_hands, key=cmp_to_key(compare))
    #print(f"DEBUG: sorted_list = {sorted_list}")

    return sorted_list

def get_total_winnings(filename):
    lines = fileutils.get_file_lines(filename)

    map_hand_to_bid = defaultdict(int)
    for l in lines:
        #print(f"DEBUG: line={l}")
        (hand, bid) = l.split()

        #print(f"DEBUG: hand={hand} bid={bid}")
        map_hand_to_bid[hand] = int(bid)

    #print(f"DEBUG: map_hand_to_bid={map_hand_to_bid}")

    sorted_hands = sort_by_rank(map_hand_to_bid.keys())

    winnings = 0
    for i in range(len(sorted_hands)):
        value = (1+i) * map_hand_to_bid[sorted_hands[i]]
        #print(f"DEBUG: value={value}")
        winnings += value

    return winnings