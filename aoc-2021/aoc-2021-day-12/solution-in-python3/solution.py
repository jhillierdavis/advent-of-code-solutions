from helpers import fileutils


from collections import defaultdict

import copy

def list_copy(orig:list) -> list:
    clone = list()
    for item in orig:
        clone.append(item)
    return clone

paths = set()

def get_path(map, parent, path:list):
    path.append(parent)
    
    children = map[parent]
    for child in children:
        if child == 'end':
            clone = list_copy(path)
            clone.append(child)
            paths.add(str(clone))
            #continue
        elif child.isupper() or child not in path:
            get_path(map, child, list_copy(path))
    return None

def get_part2_path(map, parent, path:list, small_cave_revist:bool=True):
    path.append(parent)
    
    children = map[parent]
    for child in children:
        if child == 'end':
            clone = list_copy(path)
            clone.append(child)
            paths.add(str(clone))
            #continue
        elif child.isupper():
            get_part2_path(map, child, list_copy(path), small_cave_revist)
        elif child not in path:
            get_part2_path(map, child, list_copy(path), small_cave_revist)
        elif small_cave_revist == True and 'start' != child and 'end' != child:
            small_cave_revist = False
            get_part2_path(map, child, list_copy(path), small_cave_revist)
            
    return None

def get_map_of_caves(filename):
    lines = fileutils.get_file_lines(filename)

    #map = dict()
    map = defaultdict(set)

    for l in lines:
        # print(f"DEBUG: {l}")
        pair = l.split("-")
        map[pair[0]].add(pair[1])
        map[pair[1]].add(pair[0])
    
    #print(f"DEBUG: map={map}")
    return map

def display_paths(paths):
    lines = [] 
    for l in paths:
        print(f"DEBUG: {l}")   

def count_part1_paths(filename):
    map = get_map_of_caves(filename)

    paths.clear()
    get_path(map, 'start', list())
    
    display_paths(paths)
        
    return len(paths)

def count_part2_paths(filename):
    map = get_map_of_caves(filename)

    upaths = set()    
    for k in map.keys():
        if k.islower() and k not in ['start', 'end']:
            paths.clear()
            print(f"k = {k}")
            umap = copy.deepcopy(map)
            values = umap[k]
            umap[k + '*'] = values
            for v in values:
                uvals = umap[v]
                uvals.add(k + '*')
                umap[v] = uvals
            get_path(umap, 'start', list())    
            for p in paths:                                       
                upaths.add( p.replace('*', ''))    

    display_paths(upaths)

    return len(upaths)