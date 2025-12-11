# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def find_paths(graph:dict, start:str, stop:str, current_path:list=list()) -> list[list[str]]:
    # Local path copy (for cycles detection)
    path = current_path.copy()
    path.append(start)    

    if start == stop: # Found path (from 'start') to target ('stop')
        return [path] # List of lists

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


def get_path_map_from_lines(lines:str) -> dict:
    path_map = dict()
    for l in lines:
        vals = l.split()
        path_map[vals[0][:-1]] = vals[1:]

    #logger.debug(f"path_map={path_map}")
    return path_map


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


def get_path_map_from_from_file(filename:str) -> dict:
    lines = fileutils.get_file_lines_from(filename)

    path_map = get_path_map_from_lines(lines)
    #logger.debug(f"path_map={path_map}")
    return path_map


def solve_part1(filename:str) -> int:
    path_map = get_path_map_from_from_file(filename)

    start, stop = 'you', 'out'

    paths = find_paths(path_map, start, stop)

    number_of_paths = len(paths)

    return number_of_paths


def solve_part2(filename:str) -> int:
    path_map = get_path_map_from_from_file(filename)

    svr_to_dac = find_path_count(path_map, 'svr', 'dac')
    dac_to_fft = find_path_count(path_map, 'dac', 'fft')
    fft_to_out = find_path_count(path_map, 'fft', 'out')

    svr_to_dac_to_fft_to_out = svr_to_dac * dac_to_fft * fft_to_out

    svr_to_fft = find_path_count(path_map, 'svr', 'fft')
    fft_to_dac = find_path_count(path_map, 'fft', 'dac')
    dac_to_out = find_path_count(path_map, 'dac', 'out')

    svr_to_fft_to_dac_to_out = svr_to_fft * fft_to_dac * dac_to_out

    return svr_to_dac_to_fft_to_out + svr_to_fft_to_dac_to_out


def solve_part1_using_part2_approach(filename:str) -> int:
    path_map = get_path_map_from_from_file(filename)

    return find_path_count(path_map, 'you', 'out')
