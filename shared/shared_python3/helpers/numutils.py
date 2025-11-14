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