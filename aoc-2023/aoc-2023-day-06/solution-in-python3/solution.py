from helpers import fileutils

from collections import defaultdict

def calculate_wins_using_brute_force_approach(time, distance):
    wins = 0
    for hold in range(time):
        length = hold * (time - hold)
        #print(f"{length}")
        if length > distance:
            wins += 1
    return wins


def calculate_wins_using_optimised_brute_force_approach(time, distance):
    wins = 0

    # Optimise to start win search from (existing max. distance / time) available
    start = int(distance / time )

    # Optimise to only search half the available time (as symmetric results)
    for hold in range(start, 1 + int(time/2)):
        length = hold * (time - hold)
        #print(f"hold={hold} length={length}")
        if length > distance:
            wins += 1
    
    # Adjust to cater for fact that only found half the (symmetric) answers
    wins *= 2 

    # Adjust answer if half-time availble is even
    if 0 == time % 2:        
        wins -= 1

    return wins

def calculate_wins_using_binary_search_approach(time, distance):
    return 0 # TODO