import datastructures
import fileutils

def get_map_close_to_open():
    return {'}':'{', ']':'[', ')':'(', '>':'<'}

def is_legal_chunk(chunk:str) -> bool:
    stack = datastructures.Stack()
    map_close_to_open = get_map_close_to_open()

    for ch in chunk:
        if ch in map_close_to_open.values():
           stack.push(ch)
        elif ch in map_close_to_open.keys() and stack.peek() == map_close_to_open[ch]:
            stack.pop()
        else:
            stack.push(ch)

    return stack.isEmpty()

def get_incomplete_chunk_remainder(chunk:str) -> bool:
    stack = datastructures.Stack()
    map_close_to_open = get_map_close_to_open()

    for ch in chunk:
        if ch in map_close_to_open.values():
           stack.push(ch)
        elif ch in map_close_to_open.keys() and stack.peek() == map_close_to_open[ch]:
            stack.pop()
        else:
            stack.push(ch)

    incomplete_chunk = []
    while not stack.isEmpty():
        incomplete_chunk.append(stack.pop())
    return incomplete_chunk
    


def is_corrupted_chunk(chunk:str) -> bool:
    return '' != get_corruption_char(chunk)


def get_corruption_char(chunk):
    stack = datastructures.Stack()
    map_close_to_open = get_map_close_to_open()

    for ch in chunk:
        if ch in map_close_to_open.values():
           stack.push(ch)
        elif ch in map_close_to_open.keys():
            if stack.peek() == map_close_to_open[ch]:
                stack.pop()
            else:
                return ch
        else:
            stack.push(ch)    
    return ''


def get_error_score(chunk):
    map_char_to_score = {')':3, ']':57, "}":1197, ">": 25137}

    ch = get_corruption_char(chunk)

    if ch in map_char_to_score.keys():
        return map_char_to_score[ch]
    
    return 0


def get_corruption_chunk_score_from_file(filename):
    lines = fileutils.get_file_lines(filename)

    sum = 0
    for l in lines:
        sum += get_error_score(l)
    return sum

def get_incomplete_autocomplete_score(chunk:str) -> int:
    if is_legal_chunk(chunk) or is_corrupted_chunk(chunk):
        return 0
    
    remainder = get_incomplete_chunk_remainder(chunk)

    map = { "(":1, "[":2, "{": 3, "<":4}

    #print(f"DEBUG: remainder={remainder}")

    score = 0
    for ch in remainder:
        score *= 5
        score += map[ch]

    return score


def get_middle_autocomplete_score_from_file(filename):
    lines = fileutils.get_file_lines(filename)

    scores = []
    for l in lines:
        score = get_incomplete_autocomplete_score(l)
        if score > 0:
            scores.append(score)

    sorted_scores = sorted(scores)
    return sorted_scores[ int(len(scores) / 2) ]