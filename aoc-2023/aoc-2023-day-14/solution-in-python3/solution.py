from collections import defaultdict

from helpers import fileutils, grid, point



def count_rounded_rocks_from(filename):
    lines  = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)

    return g.count_symbol('O')

def calculate_load_to_north(g):
    g = g.get_inverted_vertically()

    total_load = 0
    coords = g.get_matching_symbol_coords('O')
    for c in coords:
        total_load += 1 + c.get_y()
    return total_load

def calculate_load_from(filename):
    lines  = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    return calculate_load_to_north(g)

def shift_rounded_rocks_north(g):
    count = 0
    for col in range(1, g.get_height()):
        for row in range(g.get_width()):
            p = point.Point2D(row, col)            
            s = g.get_symbol(p)
            if s == 'O':
                p_north = point.Point2D(row, col-1)
                s_north =  g.get_symbol(p_north)
                if s_north == '.':
                    g.set_symbol(p_north, 'O')
                    g.set_symbol(p, '.')
                    count += 1
    return count

def shift_rounded_rocks_south(g):
    count = 0
    for col in range(g.get_height()-1):
        for row in range(g.get_width()):
            p = point.Point2D(row, col)            
            s = g.get_symbol(p)
            if s == 'O':
                p_north = point.Point2D(row, col+1)
                s_north =  g.get_symbol(p_north)
                if s_north == '.':
                    g.set_symbol(p_north, 'O')
                    g.set_symbol(p, '.')
                    count += 1
    return count

def shift_rounded_rocks_west(g):
    count = 0
    for col in range(g.get_height()):
        for row in range(1, g.get_width()):
            p = point.Point2D(row, col)            
            s = g.get_symbol(p)
            if s == 'O':
                p_next = point.Point2D(row-1, col)
                s_next =  g.get_symbol(p_next)
                if s_next == '.':
                    g.set_symbol(p_next, 'O')
                    g.set_symbol(p, '.')
                    count += 1
    return count

def shift_rounded_rocks_east(g):
    count = 0
    for col in range(g.get_height()):
        for row in range(g.get_width()-1):
            p = point.Point2D(row, col)            
            s = g.get_symbol(p)
            if s == 'O':
                p_next = point.Point2D(row+1, col)
                s_next =  g.get_symbol(p_next)
                if s_next == '.':
                    g.set_symbol(p_next, 'O')
                    g.set_symbol(p, '.')
                    count += 1
    return count

def solve_part1(filename):
    lines  = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    for i in range(g.get_height()-1):
        shift_rounded_rocks_north(g)     
    return calculate_load_to_north(g)

def get_repeating_sequence_in(L):
    '''Reduce the input list to a list of all repeated integers in the list.'''
    return [item for item in list(set(L)) if L.count(item) > 1]


def is_repeating_sequence_in(list_of_numbers):
    repeated_sequence = get_repeating_sequence_in(list_of_numbers)
    if len(repeated_sequence) > 0:
        print(f"DEBUG: repeated_set={repeated_sequence}")
        return True
    return False

def get_sub_sequences(seq):
    subseq_set = []
    for window_size in range(2, len(seq)):
        for i in range(len(seq) - window_size + 1):
            entry = seq[i: i + window_size]
            if not entry in subseq_set:
                subseq_set.append(entry)
    return subseq_set

def get_repeating_sequences(seq):
    subseq_set = []
    repeating_set = []
    for window_size in range(2, len(seq)):
        for i in range(len(seq) - window_size + 1):
            entry = seq[i: i + window_size]
            if not entry in subseq_set:
                subseq_set.append(entry)
            elif not entry in repeating_set:
                repeating_set.append(entry)
    return repeating_set


def solve_part2(filename):
    lines  = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    print(f"Hash of original grid = {hash(g)}")

    map_grid_to_load = {}
    load = 0
    max = 1000000000
    spin = 0
    seq_list = []
    while spin < max:
      
        for _ in range(g.get_height()-1):
            shift_rounded_rocks_north(g)     

        for _ in range(g.get_width()-1):
            shift_rounded_rocks_west(g)     

        for _ in range(g.get_height()-1):
            shift_rounded_rocks_south(g)     

        for _ in range(g.get_width()-1):
            shift_rounded_rocks_east(g)  

        hash_g = hash(g)
        load = calculate_load_to_north(g)
        if hash_g in map_grid_to_load:
            #print(f"DEBUG: spin={spin} load={load} hash_g={hash_g}")
            if hash_g in seq_list:
                remainder = max - spin
                repeat_seq_length = len(seq_list)
                offset = remainder % repeat_seq_length
                offset = offset - 1 if offset > 1 else repeat_seq_length - 1
                print(f"DEBUG: spin={spin} load={load} hash_g={hash_g} seq_list={seq_list} repeat_seq_length={repeat_seq_length} remainder={remainder} offset={offset}")
                for s in seq_list:
                    print(f"DEBUG: s={s} v={map_grid_to_load[s]}")
                return map_grid_to_load[ seq_list[offset] ]
            else:
                seq_list.append(hash_g)
        else:
            map_grid_to_load[hash_g] = load
            seq_list.clear()
        spin += 1
        
    
    return 0