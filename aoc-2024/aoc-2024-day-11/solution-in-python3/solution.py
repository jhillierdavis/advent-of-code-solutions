from helpers import fileutils

def is_even(number:int) -> bool:
    return number % 2 == 0


def count_stone_values(values:str) -> int:
    stones = values.split(' ')
    return len(stones)


def split_even_length_stone_number_into_pair(stone:int) -> (int, int):
    value = str(stone)
    midpoint = len(value)//2 
    left_value = value[:midpoint]
    right_value = value[midpoint:]
    return (int(left_value), int(right_value))


def evolve_individual_stone_number_into_pair(value:int) -> (int,int):
    if value == 0: # Value 0 -> 1 (1 stone)
        return 1, None
    
    size = len(str(value))
    if is_even(size): # Even length value -> pair of values (2 stones)
        left_value, right_value = split_even_length_stone_number_into_pair(value)
        return left_value, right_value
    
    # Default: Value -> multiplied (1 stone)
    return value * 2024, None


def evolve_stones_by_a_blink(values:str) -> str:
    separator = ' '
    line = values.split(separator)
    evolved = ''
    for v in line:
        left, right = evolve_individual_stone_number_into_pair(int(v))
        if right == None:
            evolved += str(left)
        else:
            evolved += str(left) + separator + str(right)
        evolved += separator
    return evolved.strip() # Remove last separator


def evolve_stone_values(values:str, blinks:int) -> str:
    evolved = values
    for _ in range(blinks):
        evolved = evolve_stones_by_a_blink(evolved)
    return evolved


def solve_part1(filename:str, blinks:int) -> int:
    line = fileutils.get_text_from(filename)
    evolved:str = evolve_stone_values(line, blinks)
    return count_stone_values(evolved)


def count_evolved_stones_using_cache(individual_stone_number:int, blinks:int, cache:dict) -> int:
    # Ignore lack of a stone (from evolve/split operation to stone pair, where the right stone can be 'virtual' i.e. None)
    if None == individual_stone_number: 
        return 0

    # Do not evolve (if no longer blinking)
    if blinks <= 0: 
        assert blinks == 0
        return 1 # A single individual (unevolved) stone (do not need to know/use stone number value i.e. stone count is one)

    # Use cache entry (if present)
    cache_key = (individual_stone_number, blinks)
    if cache_key in cache:
        return cache[cache_key]
    
    # Determine the number of stones that this individual stone value will evolve into (using cache for better performance)
    prior_blinks = blinks - 1 # Decrement for each evolution
    left_value, right_value = evolve_individual_stone_number_into_pair(individual_stone_number)
    number_of_stones = count_evolved_stones_using_cache(left_value, prior_blinks, cache) \
        + count_evolved_stones_using_cache(right_value, prior_blinks, cache)
    
    # Add new cache entry
    cache[cache_key] = number_of_stones
    return number_of_stones


def solve_part2(filename:str, blinks:int) -> int:    
    # Do not generate a string of values (as in Part 1) since too slow for large number of evolution steps (i.e. high number of blinks e.g. 75)
    # Instead count the number of evolved stones for each original stone number (using a cache for speed) & sum up (as answer)

    line = fileutils.get_text_from(filename)
    ans:int = 0
    cache = dict() # Cache of individual stone value, at specific blink number, mapped to count of evolved number of stones
    for v in line.split():
        individual_stone_number = int(v)
        ans += count_evolved_stones_using_cache(individual_stone_number, blinks, cache)
    return ans