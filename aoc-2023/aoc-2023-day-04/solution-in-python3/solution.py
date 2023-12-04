from helpers import fileutils

from collections import defaultdict

def get_cards_from_filename(filename):
    lines = fileutils.get_file_lines(filename)

    list_cards = []
    scratchcard = 0
    for l in lines:
        scratchcard += 1
        (c,r) = l.split(':')
        (w,h) = r.split('|')
        winning_cards = w.split()
        holding_cards = h.split()

        list_cards.append( (scratchcard, set(winning_cards), set(holding_cards)) )

    return list_cards


def solve_part1(filename):

    list_cards = get_cards_from_filename(filename)

    total = 0
    for entry in list_cards:
        points = 0
        winning_cards = entry[1]
        holding_cards = entry[2]

        # Matches = size of intersection (of 2 sets)
        matches = len(holding_cards & winning_cards) 
        if matches > 0:      
            # When there is a match: points = 2 to power of number of (matches - 1)
            points = 2**(matches-1) 

        #print(f"DEBUG: {winning_cards} {holding_cards} {points}")
        total += points

    return total


def solve_part2(filename):
    map_points = defaultdict(int)

    list_cards = get_cards_from_filename(filename) 
    for entry in list_cards:
        scratchcard = entry[0]
        winning_cards = entry[1]
        holding_cards = entry[2]
        map_points[scratchcard] += 1
        
        # Matches = size of intersection (of 2 sets)
        matches = len(holding_cards & winning_cards) 
        #print(f"DEBUG: {card} {winning_cards} {holding_cards} {matches}")

        for i in range(matches):
            winning_card = scratchcard + i + 1
            #print(f"DEBUG: Card {card} wins {wins_card}")
            map_points[winning_card] += map_points[scratchcard] 

    #print(f"DEBUG: {map_points}")
    total = 0
    for v in map_points.values():
        total += v

    return total