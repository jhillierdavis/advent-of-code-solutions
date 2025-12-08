import math

# Shared helper libraries
from helpers import fileutils, point

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_points_from_lines(lines):
    points = list()
    for l in lines:
        x,y,z = l.split(',')
        p = (int(x), int(y), int(z))
        points.append(p)

    #size = len(points)
    #logger.debug(f"points={points}")
    #logger.debug(f"size={size}")

    return points

def get_sorted_distance_pair_id_list(points):
    size = len(points)
    
    distances = list()

    for i, pi in enumerate(points):
        for j in range(i+1, size):      
            pj = points[j]      
            distance = math.dist( pi, pj) # Euclidean distance between two points p and q (see https://docs.python.org/3/library/math.html#math.dist )
            distances.append((distance, i, j))

    # Sort ascending (shortest first)
    sorted_distances = sorted(distances) 

    #logger.debug(f"Min. dist: {sorted_distances[0]} max. dist: {sorted_distances[-1]}")
    return sorted_distances


def get_matching_cicuit(circuits, idx):
    for c in circuits:
        if idx in c:
            return c
    return None


def count_cirects_connections(circuits):
    connections = 0
    for c in circuits:
        connections += len(c) - 1
    return connections


def get_circuits_lengths_sorted_decending(circuits):
    lengths = [len(c) for c in circuits]
    #lengths.append(len(remaining))
    lengths = list(set(lengths))
    lengths.sort(reverse=True)
    return lengths


def solve_part1(filename:str, connections:int):
    lines = fileutils.get_file_lines_from(filename)

    # Gather 3D points
    points = get_points_from_lines(lines)
    sorted_distance_pairs = get_sorted_distance_pair_id_list(points)

    circuits = list()
    #remaining = [i for i in range(len(points))]

    for d in sorted_distance_pairs[:connections]:
        #logger.debug(f"d={d}")
        i = d[1]
        j = d[2]

        ci = get_matching_cicuit(circuits, i)
        cj = get_matching_cicuit(circuits, j)

        if len(circuits) == 0 or (ci == None and cj == None):            
            circuits.append({i,j})
        elif ci and not cj:
            ci.add(j) 
        elif cj and not ci:
            cj.add(i)
        elif ci == cj:
            continue
        elif ci != cj:
            #raise Exception(f"ci != cj: ci={ci} cj={cj} d={d}")
            #circuits.append({i,j})
            new_circuits = list()
            merged_c = ci.union(cj)
            new_circuits.append(merged_c)
            for c in circuits:
                if c != ci and c != cj:
                    new_circuits.append(c)
            circuits = new_circuits

        """
        if i in remaining:
            remaining.remove(i)
        
        if j in remaining:
            remaining.remove(j)
        """

    lengths = get_circuits_lengths_sorted_decending(circuits)

    ans = 1
    for v in lengths[:3]:
        #logger.debug(f"v={v}")
        ans *= v
    return ans


def solve_part2(filename:str):
    lines = fileutils.get_file_lines_from(filename)

    # Gather 3D points
    points = get_points_from_lines(lines)
    size = len(points)    
    sorted_distance_pairs = get_sorted_distance_pair_id_list(points)


    circuits = list()
    
    ans = 0
    for d in sorted_distance_pairs:
        #logger.debug(f"d={d}")
        i = d[1]
        j = d[2]

        ci = get_matching_cicuit(circuits, i)
        cj = get_matching_cicuit(circuits, j)

        if len(circuits) == 0 or (ci == None and cj == None):            
            circuits.append({i,j})
        elif ci and not cj:
            ci.add(j) 
        elif cj and not ci:
            cj.add(i)
        elif ci == cj:
            continue
        elif ci != cj:
            #raise Exception(f"ci != cj: ci={ci} cj={cj} d={d}")
            #circuits.append({i,j})
            new_circuits = list()
            merged_c = ci.union(cj)
            new_circuits.append(merged_c)
            for c in circuits:
                if c != ci and c != cj:
                    new_circuits.append(c)
            circuits = new_circuits

        lengths = get_circuits_lengths_sorted_decending(circuits)
        if lengths[0] == size:
            pi = points[i]
            pj = points[j]
            ans = pi[0] * pj[0] # Multiple x coord values of last pair
            break        

    return ans