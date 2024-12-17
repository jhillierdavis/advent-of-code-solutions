import math
from functools import cache

from helpers import fileutils, numutils


def operand_combo(value, reg_map):
    if value >=0 and value <= 3:
        return value 
    if value == 4:
        return reg_map['A']
    if value == 5:
        return reg_map['B']
    if value == 6:
        return reg_map['C']
    raise Exception(f'Invalid value: {value}')


# Opcode 0
def operand_adv(value, reg_map):
    numerator = reg_map['A']
    denominator = 2 ** operand_combo(value, reg_map)
    result = int ( numerator / denominator )
    reg_map['A'] = result
    #print(f"DEBUG: [operand_adv] result={result} value={value} numerator={numerator} demoinator={denominator} reg_map={reg_map}")
    #return result


# Opcode 1
def operand_bxl(value, reg_map):
    result = reg_map['B'] ^ value
    reg_map['B'] = result
    #print(f"DEBUG: [operand_bxl] result={result} value={value} reg_map={reg_map}")
    #return result


# Opcode 2
def operand_bst(value, reg_map):
    result = operand_combo(value, reg_map) % 8
    reg_map['B'] = result
    #print(f"DEBUG: [operand_bst] result={result} value={value} reg_map={reg_map}")
    #return result


# Opcode 3
def operand_jnz(value, reg_map):
    if 0 == reg_map['A']:
        return None 
    result = value
    #print(f"DEBUG: [operand_jnz] result={result} value={value} reg_map={reg_map}")
    return result


# Opcode 4
def operand_bxc(value, reg_map):
    result = reg_map['B'] ^ reg_map['C']
    reg_map['B'] = result
    ##print(f"DEBUG: [operand_bxc] result={result} value={value} reg_map={reg_map}")
    #return result


# Opcode 5
def operand_out(value, reg_map):
    result = operand_combo(value, reg_map) % 8
    #print(f"DEBUG: [operand_out] result={result} value={value} reg_map={reg_map}")
    return result


# Opcode 6
def operand_bdv(value, reg_map):
    numerator = reg_map['A']
    denominator = 2 ** operand_combo(value, reg_map)
    result = int ( numerator / denominator )
    reg_map['B'] = result
    #print(f"DEBUG: [operand_bdv] result={result} value={value} reg_map={reg_map}")
    #return result


# Opcode 7
def operand_cdv(value, reg_map):
    numerator = reg_map['A']
    denominator = 2 ** operand_combo(value, reg_map)
    result = int ( numerator / denominator )
    reg_map['C'] = result
    #print(f"DEBUG: [operand_cdv] result={result} value={value} reg_map={reg_map}")
    #return result


#cache = {}

def process(instr_list, reg_map, offset=0):
    #print(f"DEBUG: instr_list={instr_list} {type(instr_list)}")
    result = []
    #ops = instructions.split(',')
    #size = len(ops)
    #assert offset < size

    """
    key = (instructions, reg_map['A'], reg_map['B'], reg_map['C'], offset)  
    if key in cache:
        value = cache[key]        
        #print(f"Cache key={key} value={value}")
        reg_map['A'] = value[1]
        reg_map['B'] = value[2]
        reg_map['C'] = value[3]
        return value[0]
    """

    size = len(instr_list)
    assert offset < size

    for i in range(offset, size):
        value = instr_list[i]
        if numutils.is_even(i):
            opcode = value            
        else:
            operand = value
            #print(f"DEBUG: opcode={opcode} operand={operand} reg_map={reg_map}")
            output = None
            if opcode == 0:
                output = operand_adv(value, reg_map)
            elif opcode == 1:
                output = operand_bxl(value, reg_map)
            elif opcode == 2:
                output = operand_bst(value, reg_map)
            elif opcode == 3:
                output = operand_jnz(value, reg_map)
                if output is not None:
                    sub_results_list = process(instr_list, reg_map, offset=output)
                    for item in sub_results_list:
                        result.append(item)
            elif opcode == 4:
                output = operand_bxc(value, reg_map)
            elif opcode == 5:
                output = operand_out(value, reg_map)
                result.append(output)
            elif opcode == 6:
                output = operand_bdv(value, reg_map)
            elif opcode == 7:
                output = operand_cdv(value, reg_map)

            #print(f"\n")        

    #result = result.strip(',') # Remove any last comma
    #cache[key] = (result, reg_map['A'], reg_map['B'], reg_map['C'])
    #print(f"DEBUG: result={result}")
    return result


def process_string_of_instructions(instructions:str,  reg_map, offset=0):
    instr_list = [int(item) for item in instructions.split(',')]
    #print(f"DEBUG: int_list={instr_list} type(instr_list")
    result_list = process(instr_list, reg_map, offset)
    #print(f"DEBUG: result_list={result_list}")
    return ",".join(map(str, result_list))


def get_reg_map(reg_lines):
    reg_map = {}
    for l in reg_lines:
        suffix = l[len('Register '):]
        values = suffix.split(': ')
        reg_map[values[0]] = int(values[1])    
    return reg_map


def solve_part1(filename):
    #global cache 
    #cache = {}

    #lines = fileutils.get_file_lines_from(filename)
    reg_lines = fileutils.get_lines_before_empty_from_file(filename)
    data_line = fileutils.get_lines_after_empty_from_file(filename)[0]
    #print(f"DEBUG: {reg_lines}")
    #print(f"DEBUG: {data_line}")
    
    reg_map = get_reg_map(reg_lines)
    #print(f"DEBUG: reg_map={reg_map}")

    instructions = data_line[len('Program: '):]    
    return process_string_of_instructions(instructions, reg_map)

"""
def explore_solve_part2(instructions):
    instructions = [2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0]

    last = 0
    for i in range(100000000):
        reg_map = {}
        reg_map['A'] = i
        reg_map['B'] = 0
        reg_map['C'] = 0

        #output = process(instr, new_reg_map)
        output = process(instructions, reg_map)
        a = reg_map['A']
        b = reg_map['B']
        c = reg_map['C']
        if output == [3,0] or output == [3,3,0] or output == [0,3,3,0] or output == [5,0,3,3,0] \
            or output == [5,5,0,3,3,0] or output == [3,5,5,0,3,3,0] or output == [1,3,5,5,0,3,3,0]:
            print(f"DEBUG: i={i} diff={last - i} a={a} b={b} c={c} output={output}")
            last = i
            if output == [1,3,5,5,0,3,3,0]:
                break
    return i
"""

def solve_part2(instructions):
    # Work backwards to see what taget value of Register A produced instructions values (reading from right to left)

    # NB: Both example & full instuction set includes 0 (opcode), then 3 (operand)
    #
    # Opcode: 0 -> ADV -> A = A / 2 ** 3 (operand) =  A / 8
    #
    # So, working backward do the opposite i.e. A * 8

    candidate_values = [0] # List of values to use for Register A (starting at zero)   
    for i in range(len(instructions)):
        next_candidate_values = []

        for value in candidate_values:
            # Try out addition of 0 to 7 (as 8 possibilies) to each candidate value
            for j in range(8):
                reg_map = {}                
                reg_map['B'] = 0
                reg_map['C'] = 0                
                target = (value * 8) + j
                reg_map['A'] = target

                # Check for matches (if so add to next candidate set for instruction value to left)
                if process(instructions, reg_map) == instructions[-i -1:]:
                    next_candidate_values.append(target)

        candidate_values = next_candidate_values
        #print(f'DEBUG: candidate_values={candidate_values}')

    return min(candidate_values)