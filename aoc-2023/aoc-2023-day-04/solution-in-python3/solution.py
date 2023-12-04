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

        list_cards.append( (scratchcard, winning_cards, holding_cards) )

    return list_cards


def solve_part1(filename):

    list_cards = get_cards_from_filename(filename)

    total = 0
    for entry in list_cards:
        winning_cards = entry[1]
        holding_cards = entry[2]

        points = 0
        for hc in holding_cards:
            for wc in winning_cards:
                if hc == wc:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2

        #print(f"DEBUG: {winning_cards} {holding_cards} {points}")
        total += points

    return total


def solve_part2(filename):
    map_points = defaultdict(int)

    list_cards = get_cards_from_filename(filename)

    total = 0
    for entry in list_cards:
        scratchcard = entry[0]
        winning_cards = entry[1]
        holding_cards = entry[2]
        map_points[scratchcard] += 1
        
        matches = 0
        for hc in holding_cards:
            for wc in winning_cards:
                if hc == wc:
                    matches += 1

        #print(f"DBEUG: {card} {winning_cards} {holding_cards} {matches}")

        for i in range(matches):
            wins_card = scratchcard + i + 1
            #print(f"DEBUG: Card {card} wins {wins_card}")
            map_points[wins_card] += map_points[scratchcard] 

    #print(f"DEBUG: {map_points}")
    for v in map_points.values():
        total += v

    return total