def is_even(number:int) -> bool:
    return number % 2 == 0


def is_odd(number:int) -> bool:

    return number % 2 == 1

def int_array_from_str_array(array:list[str]) -> list[int]:
    #print(f"DEBUG: {array}")
    return [int(numeric_string) for numeric_string in array]


def concatonate(alpha:int, beta:int) -> int:
    if alpha == 0:
        return beta
    return int(str(alpha) + str(beta))