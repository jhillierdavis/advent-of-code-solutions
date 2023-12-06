from helpers import fileutils

from collections import defaultdict

def solve(time, distance):
    wins = 0
    for hold in range(time):
        length = hold * (time - hold)
        print(f"{length}")
        if length > distance:
            wins += 1
    return wins