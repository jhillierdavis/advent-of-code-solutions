# Standard libs
from collections import defaultdict
import copy

# Local libs
from helpers import fileutils

def get_path(map, parent, paths, current_path:list):
    current_path.append(parent)
    
    children = map[parent]
    for child in children:
        if child == 'end':
            #clone = list_copy(path)
            clone = copy.deepcopy(current_path)
            clone.append(child)
            paths.add(str(clone))
        elif child.isupper() or child not in current_path:
            get_path(map, child, paths, copy.deepcopy(current_path))
    return None

def get_all_paths_for_map(map):
    paths = set()
    get_path(map, 'start', paths, list()) 
    return paths


def get_map_of_caves(filename):
    lines = fileutils.get_file_lines(filename)

    map = defaultdict(set)

    for l in lines:
        # print(f"DEBUG: {l}")
        pair = l.split("-")
        map[pair[0]].add(pair[1])
        map[pair[1]].add(pair[0])
    
    #print(f"DEBUG: map={map}")
    return map

def display_paths(paths):
    for l in paths:
        print(f"DEBUG: {l}")   

def count_part1_paths(filename):
    map = get_map_of_caves(filename)

    paths = get_all_paths_for_map(map)
    #display_paths(paths)
        
    return len(paths)

def count_part2_paths(filename):
    map = get_map_of_caves(filename)

    upaths = set()    
    for k in map.keys():
        if k.islower() and k not in ['start', 'end']:
            #paths.clear()
            print(f"k = {k}")
            umap = copy.deepcopy(map)
            values = umap[k]
            umap[k + '*'] = values
            for v in values:
                uvals = umap[v]
                uvals.add(k + '*')
                umap[v] = uvals
            #get_path(umap, 'start', list())    
            paths = get_all_paths_for_map(umap)
            for p in paths:                                       
                upaths.add( p.replace('*', ''))    

    display_paths(upaths)

    return len(upaths)