from collections import defaultdict
import networkx as nx

from helpers import fileutils


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


def solve_using_networkx_graph_from(filename):
    wiring_map = get_component_wiring_map_from(filename)

    partitions = get_partioned_graph_after(wiring_map, 3)  
    assert partitions
    (partition1, partition2) = partitions

    return len(partition1) * len(partition2)