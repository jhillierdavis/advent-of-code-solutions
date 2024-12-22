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


def get_subseq_to_price_map(price_sequence:list[int], change_sequence:list[int]) -> dict:
    subseq_to_price_map = dict()
    size = len(change_sequence)
    for i in range(size-3):
        changes = (change_sequence[i], change_sequence[i+1], change_sequence[i+2], change_sequence[i+3])
        if changes not in subseq_to_price_map:
            price_point = price_sequence[i+4]
#            if changes == (-2,1,-1,3):
#                print(f"DEBUG: changes={changes} price_point={price_point}")
            subseq_to_price_map[changes] = price_point

    return subseq_to_price_map


def solve_part2(filename:str) -> int:
    lines = fileutils.get_file_lines_from(filename)

    subseq_to_total_price_map = dict()
    for l in lines:
        num = int(l)
        #print(f"DEBUG: secret_number={num}")
        price_sequence = generate_secret_number_price_sequence(num, 2000)
        change_sequence = get_change_sequence(price_sequence)
        kvmap = get_subseq_to_price_map(price_sequence, change_sequence)
        for k,v in kvmap.items():
            if k in subseq_to_total_price_map:
                subseq_to_total_price_map[k] += v
            else: # First match                
                subseq_to_total_price_map[k] = v

    max_value = max(subseq_to_total_price_map.values())    

    return max_value