from functools import cmp_to_key
from collections import defaultdict

from helpers import fileutils

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
    
    return compare_same_hand_type(hand_left, hand_right)


def sort_by_rank(list_of_hands):

    #return ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']
    sorted_list = sorted(list_of_hands, key=cmp_to_key(compare))
    print(f"DEBUG: sorted_list = {sorted_list}")

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
