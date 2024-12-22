from helpers import fileutils

def mix(num, mixin):
    return mixin ^ num 

def prune(num):
    return num % 16777216

def generate_next_secret_number(initial):
    next = initial

    mixin = 64 * initial
    next = mix(next, mixin)
    next = prune(next)

    mixin = next // 32
    next = mix(next, mixin)
    next = prune(next)

    mixin = next * 2048
    next = mix(next, mixin)
    next = prune(next)

    return next


def generate_secret_number_sequence(initial, max):
    sequence = []
    next = initial
    for _ in range(max):
        next = generate_next_secret_number(next)
        sequence.append(next)
    return sequence

def generate_nth_secret_number(initial, n):
    next = initial
    for _ in range(n):
        next = generate_next_secret_number(next)
    return next


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    count = 0
    for l in lines:
        num = int(l)
        count += generate_nth_secret_number(num, 2000)

    return count

def get_last_digit(number): 
    return abs(number) % 10


def generate_secret_number_price_sequence(initial, max):
    sequence = []
    last_digit = get_last_digit(initial)
    sequence.append(last_digit)

    next = initial
    for _ in range(max-1):
        next = generate_next_secret_number(next)
        last_digit = get_last_digit(next)
        sequence.append(last_digit)
    return sequence
    

def get_change_sequence(number_sequence):
    size = len(number_sequence)
    if size <= 1: # Guard condition
        return []
    
    change_sequence = []
    for i in range(1, size):
        prior = number_sequence[i-1]
        current = number_sequence[i]
        change_sequence.append(current - prior)
    return change_sequence


def find_sequence_index(lst, sequence):
    seq_length = len(sequence)
    for i in range(len(lst) - seq_length + 1):
        if lst[i:i + seq_length] == sequence:
            return i
    return -1




def get_price_point_matching_change_sequence(secret_number, max, changes):
    ans = None
    price_sequence = generate_secret_number_price_sequence(secret_number, max)
    change_sequence = get_change_sequence(price_sequence)
    #print(f"change_sequnce={change_sequence} changes={changes}")

    index = find_sequence_index(change_sequence, changes)
    if index >= 0:
        index += 4
        #print(f"index={index} price_sequnce={price_sequence}")
        ans = price_sequence[index]
    return ans


def solve_part2(filename):

    """
    price_sequence = generate_secret_number_price_sequence(123, 10)
    print(price_sequence)
    max_value = max(price_sequence[4:])
    print(f"DEBUG: max_value={max_value}")
    index = price_sequence.index(max_value, 4)
    change_sequence = get_change_sequence(price_sequence)
    print(change_sequence[index-4])
    print(change_sequence[index-3])
    print(change_sequence[index-2])
    print(change_sequence[index-1])
    """

    
    lines = fileutils.get_file_lines_from(filename)

    count = 0
    [-2,-1]
    for l in lines:
        num = int(l)


    price_sequence = generate_secret_number_price_sequence(2024, 2000)
    print(price_sequence[:50])
    max_value = max(    )
    index = price_sequence.index(max_value, 4)
    print(f"DEBUG: num={num} max_value={max_value} index={index}")
    change_sequence = get_change_sequence(price_sequence)
    print(change_sequence[index-4])
    print(change_sequence[:50])
    print(change_sequence[index-3])
    print(change_sequence[index-2])
    print(change_sequence[index-1])


    return count