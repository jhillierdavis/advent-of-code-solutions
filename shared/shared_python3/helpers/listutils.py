
def find_shortest_sublists(list_of_lists:list[list]) -> list[list]:
    if not list_of_lists:
        return []

    # Find the length of the shortest list(s)
    min_length = min(len(lst) for lst in list_of_lists)

    # Collect all lists that have the shortest length
    shortest_lists = [lst for lst in list_of_lists if len(lst) == min_length]
    return shortest_lists


def last_index_of(lst:list, value:any) -> int:
    """
    Returns the index of the last occurrence of 'value' in the list 'lst'.
    If the value is not found, returns -1.
    """
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            return i
    return -1