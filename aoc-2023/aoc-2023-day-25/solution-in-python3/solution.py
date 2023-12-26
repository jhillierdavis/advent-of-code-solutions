from collections import defaultdict
#import sys
import networkx as nx
import random, copy

#sys.setrecursionlimit(10000) # Allow greater recursion depth (than the 1K default)!

from helpers import fileutils

"""
def get_unique_wires(wiring_map):
    wires = set()

    wires.update(wiring_map.keys())
    for k in wiring_map.keys():
        for v in wiring_map[k]:
            wires.add(v)
    return wires


def get_connected_components(wiring_map, current, group):
    for oc in wiring_map[current]:
        if oc in group:
            continue

        group.add(oc)
        get_connected_components(wiring_map, oc, group)
"""

def get_network_graph_from(wiring_map:{}) -> nx.Graph:
    # Create an undirected graph with self loops
    # https://networkx.org/documentation/stable/reference/classes/graph.html

    g = nx.Graph() 
    for k in wiring_map.keys():
        for v in wiring_map[k]:
            g.add_edge(k,v,capacity=1.0)
            g.add_edge(v,k,capacity=1.0)
    return g


def get_partioned_graph_after(wiring_map:{}, number_of_cuts:int) -> ():    
    g = get_network_graph_from(wiring_map)

    for k in [list(wiring_map.keys())[0]]:
        for v in wiring_map.keys():
            if k != v:
                # Partition & determine the number of cuts required
                # see https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.flow.minimum_cut_value.html#networkx.algorithms.flow.minimum_cut_value
                cut_value, partitions = nx.minimum_cut(g, k, v) 
                if cut_value == number_of_cuts:
                    return partitions
    return None

def get_component_wiring_map_from(filename):
    lines = fileutils.get_file_lines(filename)

    wiring_map = defaultdict(set) # component map
    for l in lines:
        k, vl = l.split(': ')
        v = vl.split()
        for e in v:
            wiring_map[k].add(e)
            wiring_map[e].add(k)

    return wiring_map

def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2

"""
def karger(G):
    length = []
    while len(G) > 2:
        v1, v2 = choose_random_key(G)
        G[v1].extend(G[v2])
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1) 
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys():
        length.append(len(G[key]))
    return length[0]
"""
"""
def karger(G):
    length = []
    while len(G) > 2:
        v1, v2 = choose_random_key(G)
        G[v1].update(G[v2])
        for x in G[v2]:
            G[x].remove(v2)
            G[x].add(v1) 
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys():
        length.append(len(G[key]))
    return length[0]
"""

def solve_using_networkx_graph_from(filename):
    wiring_map = get_component_wiring_map_from(filename)

    #print(f"DEBUG: wiring_map={wiring_map}")
    #print(f"DEBUG: wiring_map length={len(wiring_map.keys())}")

    #unique_wires = get_unique_wires(wiring_map)
    #unique_wires = get_unique_wires = wiring_map.keys()
    #print(f"DEBUG: unique_wires={unique_wires}")
    #print(f"DEBUG: unique_wires length={len(unique_wires)}")

    
    #start = next(iter(wiring_map.keys()))
    #group = set()
    #group.add(start)
    #get_connected_components(wiring_map, start, group)
    #print(f"DEBUG: group={group}")

    #for k in ['hfx','pzl', 'bvb', 'cmg', 'nvd','jqt']:
    #    print(f"DEBUG: {k} -> {wiring_map[k]}")

    """
    total = len(wiring_map.keys()) 
    x = 0
    for k in wiring_map.keys():
        count = len(wiring_map[k]) 
        if count == 4:
            print(f"{k} {count}")
            x += 1   
    
    return x * (total - x)
    """
    partitions = get_partioned_graph_after(wiring_map, 3)  
    assert partitions
    (partition1, partition2) = partitions

    return len(partition1) * len(partition2)

"""
from karger import Graph, Edge, kargerMinCut

def solve_using_kargers_algorithm_from(filename):
    wiring_map = get_component_wiring_map_from(filename)

    edge_count = len(wiring_map.keys())
    vertices_count = 0
    for k in wiring_map.keys():
        vertices_count += len(wiring_map[k])
    print(f"DEBUG: edge_count={edge_count} vertices_count={vertices_count}")

    graph = Graph(vertices_count, edge_count)
    for k in wiring_map.keys():
        for v in wiring_map[k]:
            graph.edge.append(Edge(k, v))
    
    res = kargerMinCut(graph)
    print("Cut found by Karger's randomized algo is", res)
"""


"""
    while True:
        data = copy.deepcopy(wiring_map)
        min_cut = karger(data)
        print(f"DEBUG: {data}")
        if min_cut == 3:
            return
"""

#solve_using_kargers_algorithm_from("puzzle-input-example.txt")