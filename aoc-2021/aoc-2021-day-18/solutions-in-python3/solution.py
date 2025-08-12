
def get_magnitude(snailfish_number:list) -> int:    
    left = snailfish_number[0]
    right = snailfish_number[1]
    if type(left) == list:
        left = get_magnitude(left)
    if type(right) == list:
        right = get_magnitude(right)
    return (3 * left) + (2 * right)

def add(snailfish_number_x, snailfish_number_y):
    # TODO
    return []

def add_and_reduce(snailfish_number_x, snailfish_number_y):
    # TODO
    return []

def explode(snailfish_number):
    # TODO
    return []
