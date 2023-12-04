from helpers import fileutils

from collections import defaultdict

def solve(filename):

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