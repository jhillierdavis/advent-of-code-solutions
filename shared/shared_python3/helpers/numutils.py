from typing import Callable, Any, Iterable

def is_even(number:int) -> bool:
    return number % 2 == 0


def is_odd(number:int) -> bool:

    return number % 2 == 1

def int_array_from_str_array(array:list[str]) -> list[int]:
    #print(f"DEBUG: {array}")
    return [int(numeric_string) for numeric_string in array]


def concatonate(left:int, right:int) -> int:
    if left == 0:
        return right
    return int(str(left) + str(right))


def get_middle_value_from(array_of_integers:Iterable[int]) -> int:
    size =  len(array_of_integers)
    if size <= 0: # Guard
        return None
    
    middle_index = size//2
    if size % 2 == 0: # Even length
        middle_index -= 1
    return array_of_integers[middle_index]


def is_within_range(value:int, min_value:int, max_value:int) -> bool:
    """
    Check if a numeric value is within a given inclusive range.

    Parameters:
    value (float or int): The number to check.
    min_value (float or int): The lower bound of the range.
    max_value (float or int): The upper bound of the range.

    Returns:
    bool: True if value is within [min_value, max_value], False otherwise.
    """
    return min_value <= value <= max_value


def has_repeating_half(num: int) -> bool:
    """
    Check if the given number repeats at its midpoint (e.g. 11, 22, 446446, 38593859)
    """
    s = str(num)
    size = len(s)

    if is_odd(size):
        return False # Must divide evenly

    midpoint = size // 2 
    
    left = s[0:midpoint]
    right = s[midpoint:]
    #logger.debug(f"left={left} right={right} size={size} midpoint={midpoint}")

    return left == right


def has_repeating_subsequences(num: int) -> bool:
    """
    Check if given number fully consists of repeating sub-sequences e.g. 123123123 (123 three times), 2121212121 (sequences of 21).
    """
    s = str(num)
    size = len(s)
    midpoint = size // 2

    for i in range(1, midpoint + 1):
        if size % i != 0:              
            continue # Sub-sequence length must divide evenly into whole

        subpart = s[:i]
        if subpart * (size // i) == s:
            return True # Matching sub-sequences
    return False