from helpers import fileutils

from collections import defaultdict

def calculate_wins_part1(time, distance):
    wins = 0
    for hold in range(time):
        length = hold * (time - hold)
        #print(f"{length}")
        if length > distance:
            wins += 1
    return wins


def calculate_wins_part2(time, distance):
    wins = 0

    start = int(distance / time )

    for hold in range(start, 1 + int(time/2)):
        length = hold * (time - hold)
        #print(f"hold={hold} length={length}")
        if length > distance:
            wins += 1
    wins *= 2
    if 0 == time % 2:        
        wins -= 1
    return wins