from helpers import fileutils
from collections import deque


def to_block_representation_from(diskmap):
    #print(f"DEBUG: diskmap={diskmap}")
    rep = ''

    index = 0
    for i in range(len(diskmap)):        
        ch_value = diskmap[i]
        i_value = int(ch_value)

        #print(f"DEBUG: i={i} i_value={i_value} ch_value={ch_value}")
        if i % 2 == 0: # length of file
            ch_index = str(index)
            if i_value == 0:
                rep += ch_index
            for j in range(i_value):
                rep += ch_index
            index += 1
        else: # length of free space
            for j in range(i_value):
                rep += '.'    
    return rep


def to_compacted_from(block_representation):
    rep_queue = deque([*block_representation])
    result =""
    count_space = 0
    while len(rep_queue) > 0:
        ch = rep_queue.popleft()
        if ch == '.':
            count_space += 1
            while len(rep_queue) > 0 and ch == '.':
                ch = rep_queue.pop()
            if '.' != ch:
                result += ch
        else:
            result += ch

    return result


def to_checksum_from(compacted):
    total = 0
    for i in range(len(compacted)):        
        ch_value = compacted[i]
        if '.' == ch_value:
            break 
        i_value = int(ch_value)
        #print(f"DEBUG: ch_value={ch_value} i={i}")
        total += i_value * i
        
    return total


def solve_part1(filename):
    input = fileutils.get_text_from(filename)
    block_representation = to_block_representation_from(input)
    compacted = to_compacted_from(block_representation)
    #print(f"DEBUG: compacted={compacted}")
    return to_checksum_from(compacted)


def solve_part2(filename):
    input = fileutils.get_text_from(filename)
    return "TODO"