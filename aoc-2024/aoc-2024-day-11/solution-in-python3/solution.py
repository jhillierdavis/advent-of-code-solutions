from helpers import fileutils

def is_even(number:int) -> bool:
    return number % 2 == 0


def count_stone_values(values:str) -> int:
    stones = values.split(' ')
    return len(stones)


def split_even_length_stone_number_into_pair(stone:int) -> (int, int):
    value = str(stone)
    size = len(value)//2
    left_value = value[:size]
    right_value = value[size:]
    left_value, right_value = (int(left_value), int(right_value))
    return left_value, right_value


def evolve_individual_stone_number_into_pair(value:int) -> (int,int):
    if value == 0: # 1 Stone: Value 0 -> 1 (1 stone)
        return 1, None
    
    size = len(str(value))
    if is_even(size): # Even length value -> pair of values (2 stones)
        left_value, right_value = split_even_length_stone_number_into_pair(value)
        return left_value, right_value
    else: # 1 Stone: Value multiplied (1 stone)
        return value * 2024, None


def evolve_stones_by_a_blink(values):
    line = values.split(' ')
    evolved = ''
    for v in line:
        left, right = evolve_individual_stone_number_into_pair(int(v))
        if right == None:
            evolved += str(left)
        else:
            evolved += str(left) + " " + str(right)
        evolved += ' '
    return evolved.strip()


def evolve_stone_values(values, blinks):
    evolved = values
    for _ in range(blinks):
        evolved = evolve_stones_by_a_blink(evolved)
    return evolved


def solve_part1(filename, blinks):
    line = fileutils.get_text_from(filename)
    evolved = evolve_stone_values(line, blinks)
    return count_stone_values(evolved)


def count_evolved_stones_using_cache(individual_stone_number, blinks, cache):
    if blinks <= 0: # Do not evolve
        assert blinks == 0
        return 1 # A single individual (unevolved) stone (do not need to know/use stone number value)

    # Use cache entry (if present)
    if (individual_stone_number, blinks) in cache:
        return cache[(individual_stone_number, blinks)]
    
    # Determine the number of stones that this individual stone value will evolve into (using cache for better performance)
    prior_blinks = blinks - 1
    left_value, right_value = evolve_individual_stone_number_into_pair(individual_stone_number)
    if right_value == None:
        number_of_stones = count_evolved_stones_using_cache(left_value, prior_blinks, cache)
    else:
        number_of_stones = count_evolved_stones_using_cache(left_value, prior_blinks, cache) \
            + count_evolved_stones_using_cache(right_value, prior_blinks, cache)
    
    # Add new cache entry
    cache[(individual_stone_number, blinks)] = number_of_stones
    return number_of_stones


def solve_part2(filename, blinks):    
    # Do not generate a string of values (as in Part 1) since too slow for large interactions (high number of blinks) e.g. 75
    # Instead count the number of evolved stones for each original stone number (using a cache for speed) & sum up (as answer)

    line = fileutils.get_text_from(filename)
    ans = 0
    cache = dict() # Cache of individual stone value, at specific blink number, mapped to count of evolved number of stones
    for v in line.split():
        individual_stone_number = int(v)
        ans += count_evolved_stones_using_cache(individual_stone_number, blinks, cache)
    return ans