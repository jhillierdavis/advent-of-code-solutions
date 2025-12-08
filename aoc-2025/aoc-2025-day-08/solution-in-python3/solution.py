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


def get_3d_points_from_lines(lines):
    points = list()
    for l in lines:
        x,y,z = l.split(',')
        p = (int(x), int(y), int(z))
        points.append(p)

    #size = len(points)
    #logger.debug(f"points={points}")
    #logger.debug(f"size={size}")

    return points


def get_straight_line_distance(p:tuple[int,int,int], q:tuple[int,int,int]) -> float:
    # Calculate Euclidean distance between two points p and q 
    # see https://docs.python.org/3/library/math.html#math.dist
    distance = math.dist(p, q) 
    return distance


def get_sort_asc_distance_with_3d_point_pair_ids_as_list(points:list[tuple[int,int,int]]):
    size = len(points)
    
    distance_with_3d_point_pair_ids = list()

    for i, p in enumerate(points):
        for j in range(i+1, size):      
            q = points[j]    
            distance = get_straight_line_distance(p, q)  
            distance_with_3d_point_pair_ids.append((distance, i, j))

    sorted_asc_distance_with_3d_point_pair_ids = sorted(distance_with_3d_point_pair_ids) 

    return sorted_asc_distance_with_3d_point_pair_ids


def get_matching_circuit(circuits, idx):
    for c in circuits:
        if idx in c:
            return c
    return None


def get_circuits_lengths_sorted_decending(circuits):
    lengths = [len(c) for c in circuits]
    #lengths.append(len(remaining))
    lengths = list(set(lengths))
    lengths.sort(reverse=True)
    return lengths


def connect_points_to_circuits(circuits, i, j):
    ci = get_matching_circuit(circuits, i)
    cj = get_matching_circuit(circuits, j)

    if len(circuits) == 0 or (ci == None and cj == None):            
        circuits.append({i,j})
    elif ci and not cj:
        ci.add(j) 
    elif cj and not ci:
        cj.add(i)
    elif ci != cj: # Arg! - do NOT forget to handle this case!

        #raise Exception(f"ci != cj: ci={ci} cj={cj} d={d}")
        #circuits.append({i,j})
        new_circuits = list()
        merged_c = ci.union(cj)
        new_circuits.append(merged_c)
        for c in circuits:
            if c != ci and c != cj:
                new_circuits.append(c)
        circuits = new_circuits
    # elif ci == cj: # Ignore
    
    return circuits


def create_circuits(points:list, max_conntection_pairs:int):
    sorted_asc_distance_with_3d_point_pair_ids_list = get_sort_asc_distance_with_3d_point_pair_ids_as_list(points)

    circuits = list()
    for _, i, j in sorted_asc_distance_with_3d_point_pair_ids_list[:max_conntection_pairs]: # NB: Ignore distance value (via underscore)
        circuits = connect_points_to_circuits(circuits, i, j)

    return circuits


def multiply_first_n_largest_values(value_list:list, n:int=3):
    ans = 1
    for v in value_list[:n]:
        #logger.debug(f"v={v}")
        ans *= v
    return ans


def solve_part1(filename:str, max_connections:int):
    lines = fileutils.get_file_lines_from(filename)

    points = get_3d_points_from_lines(lines)
 
    circuits = create_circuits(points, max_connections)

    lengths = get_circuits_lengths_sorted_decending(circuits)

    ans = multiply_first_n_largest_values(lengths, 3)
    return ans


def solve_part2(filename:str):
    lines = fileutils.get_file_lines_from(filename)

    points = get_3d_points_from_lines(lines)

    size = len(points)    
    sorted_asc_distance_with_3d_point_pair_ids_list = get_sort_asc_distance_with_3d_point_pair_ids_as_list(points)

    circuits = list()
        
    for _, pi, qi in sorted_asc_distance_with_3d_point_pair_ids_list: # NB: Ignore distance value (via underscore)
        circuits = connect_points_to_circuits(circuits, pi, qi)

        lengths = get_circuits_lengths_sorted_decending(circuits)

        # Check whether all points have been used to form a circuit
        if lengths[0] == size:
            # Multiple x coord values of last 3d point pair used
            ans = points[pi][0] * points[qi][0] 
            return ans        

    return 0