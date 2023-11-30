def sort_alphabetically(str):
    return ''.join(sorted(str))

def has_subset_of_chars(outer:str, inner:str):
    list_outer = list(outer)
    list_inner = list(inner)

    for ch in list_inner:
        if ch not in list_outer:
            return False
    return True