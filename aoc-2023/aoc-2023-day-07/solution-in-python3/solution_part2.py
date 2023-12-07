from functools import cmp_to_key
from collections import defaultdict

from helpers import fileutils, strutils

def get_sorted_char_freq(hand):
    freq = strutils.get_char_freq_map_from_string(hand)
    return sorted(freq.values(), reverse=True)

def get_sorted_char_freq_without_jokers(hand):
    return get_sorted_char_freq(hand.replace('J',''))

def get_joker_count(hand):
    return strutils.get_char_occurances_in_string(hand, 'J')

def get_card_value(label):
    if label.isnumeric():
        return int(label)

    if label == 'A':
        return 14
    if label == 'K':
        return 13
    if label == 'Q':
        return 12
    if label == 'T':
        return 10
    
    # Wildcard jokers
    if label == 'J':
        return 1
    
    raise ValueError("label={label}")

def is_five_of_a_kind(hand):
    jokers = get_joker_count(hand)

    if jokers == 5:
        return True

    freq = get_sorted_char_freq_without_jokers(hand)    
    max = freq[0]    
    return max + jokers >= 5

def is_four_of_a_kind(hand):
    jokers = get_joker_count(hand)

    if jokers >= 4:
        return True

    freq = get_sorted_char_freq_without_jokers(hand)
    max = freq[0]
    sum = jokers + max

    #print(f"DEBUG: hand={hand} jokers={jokers} max={max} sum={sum}")    
    return sum >= 4

def is_full_house(hand):
    jokers = get_joker_count(hand)
    if jokers >= 5:
        return True
    
    freq = get_sorted_char_freq_without_jokers(hand)
    max = freq[0]

    if jokers == 0:
        return freq == [3,2]

    if jokers == 1:
        return freq == [2,2] or freq == [3,1]

    if max + jokers >= 3:
        rem_jokers = max + jokers - 3
        #print(f"DEBUG: hand={hand} freq={freq}")
        if (len(freq) >= 2 and freq[1] + rem_jokers >= 2 ) or rem_jokers >= 2:
            return True
    return False

def is_three_of_a_kind(hand):
    jokers = get_joker_count(hand)
    if jokers >= 5:
        return True
    
    freq = get_sorted_char_freq_without_jokers(hand)
    max = freq[0]

    if jokers == 0:
        return freq == [3,1,1]

    return max + jokers >= 3

def is_two_pair(hand):
    jokers = get_joker_count(hand)
    if jokers >= 5:
        return True
    
    freq = get_sorted_char_freq_without_jokers(hand)
    max = freq[0]

    if jokers == 0:
        return freq == [2,2,1]

    if jokers == 1:
        return freq == [2,1,1]

    if max + jokers >= 2:
        rem_jokers = max + jokers - 2
        if (len(freq) >= 2 and freq[1] + rem_jokers >= 2 ) or rem_jokers >= 2:
            return True
    return False

def is_one_pair(hand):
    jokers = get_joker_count(hand)
    if jokers >= 5:
        return True
    
    freq = get_sorted_char_freq_without_jokers(hand)
    max = freq[0]

    if jokers == 0:
        return freq == [2,1,1,1]
    
    return max + jokers >= 2

def is_distinct(hand):
    jokers = get_joker_count(hand)
    if jokers >= 5:
        return True
    
    freq = get_sorted_char_freq_without_jokers(hand)
    max = freq[0]

    if jokers == 0:
        return freq == [1,1,1,1,1]
    
    return max + jokers >= 1


def get_hand_type(hand):
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

    return 6


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


def sort_by_rank_with_wildcard_jokers(list_of_hands):
    sorted_list = sorted(list_of_hands, key=cmp_to_key(compare))
    #print(f"DEBUG: sorted_list = {sorted_list}")
    return sorted_list

def get_total_winnings_with_wildcard_jokers(filename):
    lines = fileutils.get_file_lines(filename)

    map_hand_to_bid = defaultdict(int)
    for l in lines:
        #print(f"DEBUG: line={l}")
        (hand, bid) = l.split()

        #print(f"DEBUG: hand={hand} bid={bid}")
        map_hand_to_bid[hand] = int(bid)

    #print(f"DEBUG: map_hand_to_bid={map_hand_to_bid}")

    sorted_hands = sort_by_rank_with_wildcard_jokers(map_hand_to_bid.keys())

    winnings = 0
    for i in range(len(sorted_hands)):
        value = (1+i) * map_hand_to_bid[sorted_hands[i]]
        #print(f"DEBUG: value={value}")
        winnings += value

    return winnings