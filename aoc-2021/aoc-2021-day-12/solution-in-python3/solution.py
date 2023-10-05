from helpers import fileutils

from collections import defaultdict

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
            continue
        elif child.isupper() or child not in path:
            get_path(map, child, list_copy(path))
    return None


def count_paths(filename):
    

    lines = fileutils.get_file_lines(filename)

    #map = dict()
    map = defaultdict(set)

    for l in lines:
        print(f"DEBUG: {l}")
        pair = l.split("-")
        map[pair[0]].add(pair[1])
        map[pair[1]].add(pair[0])

    print(f"DEBUG: map={map}")

    paths.clear()
    get_path(map, 'start', list())
    for path in paths:
        print(f"DEBUG: path={path}")
        
    return len(paths)