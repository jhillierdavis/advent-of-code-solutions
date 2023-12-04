from helpers import fileutils

from collections import defaultdict

def get_card_matches_from_filename(filename):
    lines = fileutils.get_file_lines(filename)

    list_card_matches = []
    scratchcard = 0
    for l in lines:
        scratchcard += 1
        (c,r) = l.split(':')
        (w,h) = r.split('|')
        winning_cards = w.split()
        holding_cards = h.split()

        # Number of card matches = size of intersection (of 2 sets; winning cards & holding cards)
        matches = len(set(holding_cards) & set(winning_cards))

        list_card_matches.append(matches)

    return list_card_matches


def solve_part1(filename):

    list_card_matches = get_card_matches_from_filename(filename)

    total = 0
    for matches in list_card_matches:
        if matches > 0:      
            # When there is a match: points = 2 to power of number of (matches - 1)
            total += 2**(matches-1)
    return total


def solve_part2(filename):
    map_points = defaultdict(int)

    list_card_matches = get_card_matches_from_filename(filename) 
    scratchcard = 0
    for matches in list_card_matches:
        scratchcard += 1
        map_points[scratchcard] += 1
        
        for i in range(matches):
            winning_card = scratchcard + i + 1
            map_points[winning_card] += map_points[scratchcard] 

    #print(f"DEBUG: {map_points}")
    total = 0
    for v in map_points.values():
        total += v

    return total