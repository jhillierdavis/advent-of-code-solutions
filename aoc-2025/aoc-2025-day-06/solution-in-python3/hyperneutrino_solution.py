###
# Efficent / succint solution example from HyperNeutrino (with my own comments)
# 
# See:
# 
# https://www.youtube.com/watch?v=JVCTxubqLqE
# https://github.com/hyperneutrino/advent-of-code/blob/main/2025/day-06
#
###

def solve_part1(filename):
    # reads a file, transposes its contents, treats each column as an arithmetic expression (numbers followed by an operator), evaluates it, and sums the results.

    lines = [line.strip().split() for line in open(filename, 'r')] # Read input data
    cols = list(zip(*lines)) # Transposes rows into columns 

    total = 0
    for *nums, op in cols: # *nums → all elements except the last one, op → last element 
        total += eval(op.join(nums)) #Evaluates the string as a Python expression

    return total


def solve_part2(filename):
    # reads a text grid from a file, splits it into groups of columns separated by blank spaces, reconstructs arithmetic expressions from those groups, evaluates them, and returns the total sum.
    
    grid = [line.strip("\n") for line in open(filename)]
    cols = list(zip(*grid))

    groups = []
    group = []

    for col in cols:
        if set(col) == {" "}: # If the column is entirely spaces treat it as a separator
            groups.append(group)
            group = []
        else:
            group.append(col)

    groups.append(group)

    total = 0

    for group in groups:
        total += eval(group[0][-1].join("".join(line[:-1]) for line in group))

    return total