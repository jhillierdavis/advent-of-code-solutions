def sort_alphabetically(str):
    return ''.join(sorted(str))

def has_subset_of_chars(outer:str, inner:str):
    list_outer = list(outer)
    list_inner = list(inner)

    for ch in list_inner:
        if ch not in list_outer:
            return False
    return True

def get_char_freq_map_from_string(source) -> map:
    freq = {}
    for c in set(source):
       freq[c] = source.count(c)
    return freq

def get_char_occurances_in_string(source:str, target:chr) -> int:
    occurances = 0
    for i in range(len(source)):
        if target == source[i]:
            occurances += 1
    return occurances

def string_to_int_list(line):
    return list(map(int, line.split()))
