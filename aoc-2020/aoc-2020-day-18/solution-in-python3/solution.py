# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

import re

INNERMOST_PARENTHESES_REGEXP = re.compile(r'\(([^()]+)\)')


def compute_value(expression):
    #logger.debug(f"expression={expression}")
    tokens = expression.split(' ')

    return calculate_result(tokens)


def substitution_innermost_parenthesises_expression_with_value(match):
    value = match[0][1:-1] # Remove parenthesis
    return str(compute_value(value))


def replace_parenthesis_values(expression):
    while INNERMOST_PARENTHESES_REGEXP.search(expression):
        expression = INNERMOST_PARENTHESES_REGEXP.sub(substitution_innermost_parenthesises_expression_with_value, expression)
    return expression


def compute_expression(expression):
    exp = replace_parenthesis_values(expression)
    return compute_value(exp)


def calculate(result, operator, val):
    if operator == '+':
        result += val
    elif operator == '*':
        result *= val                
    else:
        result = val
    return result


def calculate_result(tokens:list[str]) -> int:
    result = 0        
    operator = None
    offset = 0
    for t in tokens:
        if offset > 0:
            offset -= 1
            continue

        if t == '+':
            operator = '+'
        elif t == '*':
            operator = '*'
        else:
            val = int(t)
            result = calculate(result, operator, val)
            operator = None
        #logger.debug(f"t={t} result={result}")
    return result


def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    ans = 0
    for l in lines:
        ans += compute_expression(l)
    return ans


ADDITION_REGEXP = re.compile(r'(\d+) \+ (\d+)')


def substitute_addition(match):
    return str(int(match[1]) + int(match[2]))


def compute_value_with_addition_precedence(expression):
    #logger.debug(f"expression={expression}")
    while ADDITION_REGEXP.search(expression):
        expression = ADDITION_REGEXP.sub(substitute_addition, expression)
        #logger.debug(f"expression={expression}")

    tokens = expression.split(' ')

    return calculate_result(tokens)


def substitution_innermost_parenthesises_expression_then_addition_with_value(match):
    value = match[0][1:-1] # Remove parenthesis
    return str(compute_value_with_addition_precedence(value))


def replace_parenthesis_then_addition_values(expression):
    while INNERMOST_PARENTHESES_REGEXP.search(expression):
        expression = INNERMOST_PARENTHESES_REGEXP.sub(substitution_innermost_parenthesises_expression_then_addition_with_value, expression)
    return expression


def compute_advanced_expression(expression):
    exp = replace_parenthesis_then_addition_values(expression)
    return compute_value_with_addition_precedence(exp)


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    ans = 0
    for l in lines:
        ans += compute_advanced_expression(l)
    return ans
