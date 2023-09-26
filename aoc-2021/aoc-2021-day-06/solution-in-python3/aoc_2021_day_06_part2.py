# Use defaultdict() instead of dict() to avoid KeyError (e.g. on initialisation, when key not already set)
from collections import defaultdict

def populate_map_fish_age_to_fish_count(initial_fish_ages:[int]):
    map_fishes = defaultdict(int) # Default items (keys) are created using int(), which will return the integer object (value) 0

    for entry in initial_fish_ages:
        map_fishes[entry] += 1

    return map_fishes

# For each passing day map the fish's age to a corresponding count (i.e. the numeber of fish of that age)
def get_number_of_fish_after_elapsed_days(initial_fish_ages:[int], days:int):
    map_fish_age_to_count = populate_map_fish_age_to_fish_count(initial_fish_ages)

    for day in range(days):
        map_fish_age_to_count_updated = defaultdict(int)

        for fish_age, fish_count in map_fish_age_to_count.items():
            # Add the last day's fish count to the current day's fish age
            if fish_age == 0:                
                map_fish_age_to_count_updated[6] += fish_count
                map_fish_age_to_count_updated[8] += fish_count
            else:
                map_fish_age_to_count_updated[fish_age - 1] += fish_count
        map_fish_age_to_count = map_fish_age_to_count_updated
            
    return sum(map_fish_age_to_count.values())