import re

# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_equation_map_from_lines(lines):
    eq_map = dict()

    for i, l in enumerate(lines):
        values = re.split(" +",l)
        #logger.debug(f"values={values}")

        if not (values[0] == '*' or  values[0] == '+'):
            int_vals = list()
            for v in values:
                int_vals.append(int(v))
            #logger.debug(f"int_val={int_vals}")
            eq_map[i] = int_vals
        else:
            eq_map[i] = values

    return eq_map


def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    eq_map = get_equation_map_from_lines(lines)
    
    #logger.debug(f"eq_map={eq_map}")

    size = len(eq_map)

    op_idx = size - 1
    operators = eq_map[op_idx]
    #logger.debug(f"operators={operators}")
    #for i in range(size-2):

    ans = 0
    
    for i, op in enumerate(operators):
        result = 0
        if op == '*':
            result = 1
        elif op == '+':
            result = 0
        else:
            raise Exception(f"Unknown operator={op}")


        for x in range(op_idx):
            vals = eq_map[x]

            if op == '*':
                result *= vals[i]
            elif op == '+':
                result += vals[i]
            else:
                raise Exception(f"Unknown operator={op}")
        
        #logger.debug(f"i={i} op={op} result={result} ans={ans}")
        ans += result

    return ans


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)
    return "TODO"
