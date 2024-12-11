from helpers import fileutils, numutils


def is_possible_equation(values, result, subtotal=0, use_concationation=False):    
    if subtotal > result:
        return False
    
    addition = values[0] + subtotal
    multiplication = values[0] if subtotal == 0 else values[0] * subtotal # Fix nasty bug! (Originally forgot to guard against multiplication by zero!)    
    concatination = numutils.concatonate(subtotal, values[0]) if use_concationation else None
    
    size = len(values)
    if size == 1:
        if result == addition or result == multiplication or (use_concationation and result == concatination):
            return True
        return False

    if is_possible_equation(values[1:], result, addition, use_concationation) \
        or is_possible_equation(values[1:], result, multiplication, use_concationation) \
        or (use_concationation and is_possible_equation(values[1:], result, concatination, use_concationation)):
            return True
    return False


def is_possible_equation_with_concatonation(values, result, subtotal=0):
    return is_possible_equation(values, result, subtotal, True)


def count_valid_target_result_for_expression_values_from(filename, use_concationation=False):
    lines = fileutils.get_file_lines_from(filename)
    ans = 0
    for l in lines:
        parts = l.split(': ')
        result = int(parts[0])
        values = numutils.int_array_from_str_array(parts[1].split(' '))

        if is_possible_equation(values, result, 0, use_concationation):
            #print(f"DEBUG: Valid equation: {result} {values}")
            ans += result
    return ans    


def solve_part1(filename):
    return count_valid_target_result_for_expression_values_from(filename)


def solve_part2(filename):
    return count_valid_target_result_for_expression_values_from(filename, True)