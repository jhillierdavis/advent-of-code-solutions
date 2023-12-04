from helpers import fileutils

from collections import defaultdict

def solve_part1(filename):

    lines = fileutils.get_file_lines(filename)

    total = 0
    for l in lines:
        

        (c,r) = l.split(':')

        (w,h) = r.split('|')

        #print(f"DBEUG: {w} {h}")

        winning_cards = w.split()
        holding_cards = h.split()

        points = 0
        for hc in holding_cards:
            for wc in winning_cards:
                if hc == wc:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2

        print(f"DBEUG: {winning_cards} {holding_cards} {points}")

        total += points

    return total


def solve_part2(filename):

    lines = fileutils.get_file_lines(filename)

    map_points = defaultdict(int)

    total = 0
    card = 0
    for l in lines:
        card += 1
        map_points[card] += 1
        

        (c,r) = l.split(':')

        (w,h) = r.split('|')

        #print(f"DBEUG: {w} {h}")

        winning_cards = w.split()
        holding_cards = h.split()

        
        matches = 0
        for hc in holding_cards:
            for wc in winning_cards:
                if hc == wc:
                    matches += 1

        #print(f"DBEUG: {card} {winning_cards} {holding_cards} {matches}")

        for i in range(matches):
            wins_card = card+i+1
            #print(f"DEBUG: Card {card} wins {wins_card}")
            map_points[wins_card] += map_points[card] 

        
        

    #print(f"DEBUG: {map_points}")

    for v in map_points.values():
        total += v

    return total