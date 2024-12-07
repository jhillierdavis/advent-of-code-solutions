from helpers import fileutils

def to_int_array_from(array_str):
    #print(f"DEBUG: {array_str}")
    values = [int(numeric_string) for numeric_string in array_str]
    return values

def is_possible_equation(values, result, subtotal=0):    
    if subtotal > result:
        return False
    
    addition = values[0] + subtotal
    multiplication = values[0] if subtotal == 0 else values[0] * subtotal # Fix nasty bug (originally forgot to guard against multiplication by zero)!
    
    size = len(values)
    if size == 1:
        if result == addition or result == multiplication:
            return True
        return False

    if is_possible_equation(values[1:], result, addition) or is_possible_equation(values[1:], result, multiplication):
        return True  


def concatonate(alpha:int, beta:int) -> int:
    if alpha == 0:
        return beta
    return int(str(alpha) + str(beta))


def is_possible_equation_with_concatonation(values, result, subtotal=0):
    #print(f"DEBUG: subtotal={subtotal} values={values}")
    
    if subtotal > result:
        return False
    
    addition = values[0] + subtotal
    multiplication = values[0] if subtotal == 0 else values[0] * subtotal # Fix nasty bug (originally forgot to guard against multiplication by zero)!
    concatination = concatonate(subtotal, values[0])
    
    
    size = len(values)
    if size == 1: # Last value
        if result == addition or result == multiplication or result == concatination:
            #print(f"DEBUG: Valid subtotal={subtotal} values={values}")
            return True
        return False

    if is_possible_equation_with_concatonation(values[1:], result, addition) \
        or is_possible_equation_with_concatonation(values[1:], result, multiplication) \
        or is_possible_equation_with_concatonation(values[1:], result, concatination):
            return True
    return False


"""
def is_possible_equation_with_concatonation(values, result, subtotal=0):
    print(f"DEBUG: subtotal={subtotal} values={values} result={result}")
    
    if subtotal > result:
        return False
    
    size = len(values)
    if size == 1:
        if result == concatonate(subtotal, values[0]):
            return True
        return False

    return is_possible_equation(values[1:], result, concatonate(subtotal, values[0]))
"""

def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)
    ans = 0
    for l in lines:
        parts = l.split(': ')
        result = int(parts[0])
        values = to_int_array_from(parts[1].split(' '))

        if is_possible_equation(values, result):
            #print(f"DEBUG: Valid equation: {result} {values}")
            ans += result
    return ans


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    ans = 0
    for l in lines:
        parts = l.split(': ')
        result = int(parts[0])
        values = to_int_array_from(parts[1].split(' '))

        if is_possible_equation_with_concatonation(values, result):
            print(f"DEBUG: Valid equation: {result} {values}")
            ans += result
        #else:
        #    print(f"DEBUG: Invalid equation: {result} {values}")
    return ans