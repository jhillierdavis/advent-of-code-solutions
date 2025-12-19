
def set_bitmask_bit_at_index(bitmask, index):
    assert type(index) == int
    """
    Set the bit at the given index in the bitmask.

    Parameters:
    - bitmask: integer representing the current bitmask
    - index: position of the bit to set (0 = least significant bit)

    Returns:
    - Updated bitmask with the bit at 'index' set to 1
    """
    return bitmask | (1 << index)


def is_bitmask_bit_set_at_index(bitmask, index):
    """
    Check if the bit at a given index is set to 1 in the bitmask.

    Parameters:
    - bitmask: integer representing the bitmask
    - index: position of the bit to check (0 = least significant bit)

    Returns:
    - True if the bit at 'index' is 1, False otherwise
    """
    return (bitmask & (1 << index)) != 0


def strings_to_bitmask(strings, universe):
    """
    Convert a list of strings into a bitmask.

    Parameters:
    - strings: list of strings to encode
    - universe: list of all possible strings (defines bit positions)

    Returns:
    - bitmask: integer representing the set of strings
    """
    bitmask = 0
    for s in strings:
        if s in universe:
            idx = universe.index(s)   # position of string in universe
            bitmask |= (1 << idx)     # set the bit at that position
    return bitmask

def bitmask_to_strings(bitmask, universe):
    """
    Convert a bitmask back into a list of strings.

    Parameters:
    - bitmask: integer bitmask
    - universe: list of all possible strings (defines bit positions)

    Returns:
    - strings: list of strings represented by the bitmask
    """
    strings = []
    for idx, s in enumerate(universe):
        if bitmask & (1 << idx):
            strings.append(s)
    return strings

