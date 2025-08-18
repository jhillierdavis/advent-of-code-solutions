import math

def get_magnitude(snailfish_number:list) -> int:   
    # obtain the calculated magnitude of a snailfish number 
    left = snailfish_number[0]
    right = snailfish_number[1]
    if type(left) == list:
        left = get_magnitude(left)
    if type(right) == list:
        right = get_magnitude(right)
    return (3 * left) + (2 * right)

def add(snailfish_number_x, snailfish_number_y):
    # add 2 snailfish numbers
    result = []
    result.append(snailfish_number_x)
    result.append(snailfish_number_y)
    return result

def add_and_reduce(snailfish_number_x, snailfish_number_y):
    # TODO
    return []

def split(number:int):
    if number > 9:
        half = number/2
        return [math.floor(half), math.ceil(half)]
    return number

def calculate_eplosion(snailfish_number, depth):
    if depth == 4:
        return 0
    return snailfish_number

def generate_explosion(snailfish_number):
    #print(f"DEBUG: {snailfish_number}")
    left = snailfish_number[0]
    right = snailfish_number[1]
    if type(left) == list and type(right) == int:
        return [0, left[1] + right]
    if type(right) == list and type(left) == int:
        return [left + right[0], 0]
    raise Exception(f"Failed to explode unexpected snailfish_number={snailfish_number}")
    #return [] # Not expected!
    
"""
def explode(snailfish_number, depth=0):
    result = []

    for e in snailfish_number:
        #print(f"DEBUG: e={e}, depth={depth}, result={result}")
        if type(e) == int:
            result.append(e)
        else:
            if depth < 3:
                result.append(explode(e, depth+1))
            else:
                #result.append(generate_explosion(e))
                result.append(0)
    return result
"""

def find_and_explode(snailfish_number, depth=0):
    result = []
    left = 0
    right = 0

    for e in snailfish_number:
        #print(f"DEBUG: e={e}, depth={depth}, result={result}")
        if type(e) == int:
            if right > 0:
                result.append(e + right)
                right = 0
            else:
                result.append(e)
        else:
            if depth < 3:
                subresult, left, right = find_and_explode(e, depth+1)
                result.append(subresult)
            else:
                #result.append(generate_explosion(e))
                left = e[0]
                right = e[1]
                result.append(0)
    return result, left, right


def explode(snailfish_number):
    result, left, right = find_and_explode(snailfish_number)

    return result