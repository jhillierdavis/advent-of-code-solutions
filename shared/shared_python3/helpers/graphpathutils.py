from helpers import bitmaskutils


def find_paths(graph:dict, start:str, stop:str, current_path:list=list()) -> list[str]:
    """
    Find all unique paths from start to end in a graph.

    Parameters:
    - graph: dict mapping parent -> list of children (strings)
    - start: starting parent node (string)
    - stop: target child node (string)
    - path: current traversal path (used internally)

    Returns:
    - List of paths, where each path is a list of nodes (strings)
    """

    # Local path copy (for cycles detection)
    path = current_path.copy()
    path.append(start)    

    if start == stop: # Found path (from 'start') to target ('stop')
        return [path]

    if start not in graph: # Childless
        return list() # Empty path

    child_paths = list()
    for child in graph[start]:
        
        if child in path: # Avoid cycles
            continue

        new_paths = find_paths(graph, child, stop, path)
        for p in new_paths:
            child_paths.append(p)

    return child_paths


def find_path_count(path_map:dict, start:str, stop:str) -> int:
    from functools import cache

    # Cannot cache collections (dict, list etc.), so use inner function:

    @cache
    def cachable_find_path_count(start, stop):
        if start == stop:
            return 1
        
        if start not in path_map: # Childless
            return 0   

        count = 0
        for child in path_map[start]:  
            count += cachable_find_path_count(child, stop)

        return count
            
    return cachable_find_path_count(start, stop)


def find_path_count_including_all_intermediates(path_map:dict, start:str, stop:str, intermediates=set()) -> int:       
    if type(intermediates) == list:
        # Ensure a set type for uniqueness of entries
        intermediates = set(list)    
    include_list = list(intermediates) # Use a list for indexing

    # Convert a collection into a bitmask so that can be cached (unlike list or set collections)
    initial_bitmask = bitmaskutils.create_empty_bitmask_of_size(len(include_list))
    target_bitmask = initial_bitmask
    for i, _ in enumerate(include_list):
        #logger.debug(f"target_bitmask={target_bitmask} i={i} include_list={include_list}")
        target_bitmask = bitmaskutils.set_bitmask_bit_at_index(int(target_bitmask), i)
    
    if len(intermediates) > 0:
        assert initial_bitmask != target_bitmask, f"initial_bitmask={initial_bitmask} target_bitmask={target_bitmask}"

    from functools import cache

    @cache
    def cachable(start, stop, path_bitmask):
        # Check whether at target child 'stop'
        if start == stop:
            if path_bitmask == target_bitmask: # Matched with intermediates
                return 1 
            return 0        

        # Check whether childless
        if start not in path_map:
            return 0

        # Recurse through all children
        count = 0
        for child in path_map[start]:            
            child_bitmask = path_bitmask
            if child in include_list:
                idx = include_list.index(child)
                #logger.debug(f"idx={idx} child={child}")
                child_bitmask = bitmaskutils.set_bitmask_bit_at_index(int(child_bitmask), idx)
            count += cachable(child, stop, child_bitmask)

        return count
            
    return cachable(start, stop, initial_bitmask)
