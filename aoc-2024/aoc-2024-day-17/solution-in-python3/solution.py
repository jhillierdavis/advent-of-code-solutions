import math

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
    print(f"DEBUG: [operand_adv] result={result} value={value} numerator={numerator} demoinator={denominator} reg_map={reg_map}")
    return result


# Opcode 1
def operand_bxl(value, reg_map):
    result = reg_map['B'] ^ value
    reg_map['B'] = result
    print(f"DEBUG: [operand_bxl] result={result} value={value} reg_map={reg_map}")
    return result


# Opcode 2
def operand_bst(value, reg_map):
    result = operand_combo(value, reg_map) % 8
    reg_map['B'] = result
    print(f"DEBUG: [operand_bst] result={result} value={value} reg_map={reg_map}")
    return result


# Opcode 3
def operand_jnz(value, reg_map):
    if 0 == reg_map['A']:
        return None 
    result = value
    print(f"DEBUG: [operand_jnz] result={result} value={value} reg_map={reg_map}")
    return result

# Opcode 4
def operand_bxc(value, reg_map):
    result = reg_map['B'] ^ reg_map['C']
    reg_map['B'] = result
    print(f"DEBUG: [operand_bxc] result={result} value={value} reg_map={reg_map}")
    return result


# Opcode 5
def operand_out(value, reg_map):
    result = operand_combo(value, reg_map) % 8
    print(f"DEBUG: [operand_out] result={result} value={value} reg_map={reg_map}")
    return result

# Opcode 6
def operand_bdv(value, reg_map):
    numerator = reg_map['A']
    denominator = 2 ** operand_combo(value, reg_map)
    result = int ( numerator / denominator )
    reg_map['B'] = result
    print(f"DEBUG: [operand_bdv] result={result} value={value} reg_map={reg_map}")
    return result

# Opcode 7
def operand_cdv(value, reg_map):
    numerator = reg_map['A']
    denominator = 2 ** operand_combo(value, reg_map)
    result = int ( numerator / denominator )
    reg_map['C'] = result
    print(f"DEBUG: [operand_cdv] result={result} value={value} reg_map={reg_map}")
    return result


def process(instructions, reg_map, offset=0):
    

    result = ""
    ops = instructions.split(',')
    size = len(ops)
    assert offset < size

    for i in range(offset, len(ops)):
        value = int(ops[i])
        if numutils.is_even(i):
            opcode = value            
        else:
            operand = value
            print(f"DEBUG: opcode={opcode} operand={operand} reg_map={reg_map}")
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
                    result += process(instructions, reg_map, offset=output)
            elif opcode == 4:
                output = operand_bxc(value, reg_map)
            elif opcode == 5:
                output = operand_out(value, reg_map)
                result += str(output) + ','
            elif opcode == 6:
                output = operand_bdv(value, reg_map)
            elif opcode == 7:
                output = operand_cdv(value, reg_map)

            print(f"\n")
            


    return result.strip(',') # Remove any last comma


def solve_part1(filename):
    #lines = fileutils.get_file_lines_from(filename)
    reg_lines = fileutils.get_lines_before_empty_from_file(filename)
    data_line = fileutils.get_lines_after_empty_from_file(filename)[0]
    #print(f"DEBUG: {reg_lines}")
    #print(f"DEBUG: {data_line}")

    
    reg_map = {}
    for l in reg_lines:
        suffix = l[len('Register '):]
        values = suffix.split(': ')
        reg_map[values[0]] = int(values[1])
    print(f"DEBUG: reg_map={reg_map}")

    #print(f"DEBUG: {reg_lines}")

    instr = data_line[len('Program: '):]    
    return process(instr, reg_map)


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    return "TODO"