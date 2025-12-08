import math

# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_3d_points_from_lines(lines:str) -> list[tuple[int,int,int]]:
    points = [tuple(map(int, l.split(','))) for l in lines]
    return points


def get_straight_line_distance(p:tuple[int,int,int], q:tuple[int,int,int]) -> float:
    # Calculate Euclidean distance between two points p and q 
    # see https://docs.python.org/3/library/math.html#math.dist
    distance = math.dist(p, q) 
    return distance


def get_sort_asc_distance_with_3d_point_pair_ids_as_list(points:list[tuple[int,int,int]]) -> list[tuple[int,int,int]]:
    size = len(points)
    
    distance_with_3d_point_pair_ids = list()

    for i, p in enumerate(points):
        for j in range(i+1, size):      
            q = points[j]    
            distance = get_straight_line_distance(p, q)  
            distance_with_3d_point_pair_ids.append((distance, i, j))

    sorted_asc_distance_with_3d_point_pair_ids = sorted(distance_with_3d_point_pair_ids) 

    return sorted_asc_distance_with_3d_point_pair_ids


def get_matching_circuit(circuits:list[set[int]], idx:int) -> set[int]|None:
    for c in circuits:
        if idx in c:
            return c
    return None


def get_circuits_lengths(circuits:list[set[int]]) -> list[int]:
    lengths = [len(c) for c in circuits]
    return lengths


def connect_points_to_circuits(circuits:list[set[int]], i:int, j:int) -> list[set[int]]:
    ci = get_matching_circuit(circuits, i)
    cj = get_matching_circuit(circuits, j)

    if len(circuits) == 0 or (ci == None and cj == None):            
        circuits.append({i,j})
    elif ci and not cj:
        ci.add(j) 
    elif cj and not ci:
        cj.add(i)
    elif ci != cj: # Arg! - do NOT forget to handle this case!

        new_circuits = list()
        merged_c = ci.union(cj)
        new_circuits.append(merged_c)
        for c in circuits:
            if c != ci and c != cj:
                new_circuits.append(c)
        circuits = new_circuits
    # elif ci == cj: # Ignore
    
    return circuits


def create_circuits(points:list[tuple[int,int,int]], max_conntection_pairs:int) -> list[set[int]]:
    sorted_asc_distance_with_3d_point_pair_ids_list = get_sort_asc_distance_with_3d_point_pair_ids_as_list(points)

    circuits = list()
    for _, i, j in sorted_asc_distance_with_3d_point_pair_ids_list[:max_conntection_pairs]: # NB: Ignore distance value (via underscore)
        circuits = connect_points_to_circuits(circuits, i, j)

    return circuits


def multiply_first_n_largest_values(value_list:list[int], n:int=3) -> int:
    # Sort unique values in ascending order
    sorted_asc_values = list(set(value_list))
    sorted_asc_values.sort(reverse=True)

    size = len(sorted_asc_values) 
    assert size >= n ,f"size={size} n={n}"

    ans = 1
    for v in sorted_asc_values[:n]:
        #logger.debug(f"v={v}")
        ans *= v
    return ans


def solve_part1(filename:str, max_connections:int) -> int:
    lines = fileutils.get_file_lines_from(filename)

    points = get_3d_points_from_lines(lines)
 
    circuits = create_circuits(points, max_connections)

    circuit_lengths = get_circuits_lengths(circuits)

    ans = multiply_first_n_largest_values(circuit_lengths, 3)
    return ans


def solve_part2(filename:str) -> int:
    lines = fileutils.get_file_lines_from(filename)

    points = get_3d_points_from_lines(lines)

    size = len(points)    
    sorted_asc_distance_with_3d_point_pair_ids_list = get_sort_asc_distance_with_3d_point_pair_ids_as_list(points)

    circuits = list()
        
    for _, pi, qi in sorted_asc_distance_with_3d_point_pair_ids_list: # NB: Ignore distance value (via underscore)
        circuits = connect_points_to_circuits(circuits, pi, qi)

        lengths = get_circuits_lengths(circuits)

        # Check whether all points have been used to form a circuit
        if max(lengths) == size:
            # Multiple x coord values of last 3d point pair used
            ans = points[pi][0] * points[qi][0] 
            return ans        

    raise Exception("No circuit formed using all points!")