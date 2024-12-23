from helpers import fileutils


def add_to_map(comp_map, this_comp, other_comp):
    
    if this_comp in comp_map:
        linked = comp_map[this_comp]       
        linked.add(other_comp)
    else:
        linked = set()
        linked.add(other_comp)
        comp_map[this_comp] = linked


def get_computer_map(filename):
    lines = fileutils.get_file_lines(filename)    
    computer_map = dict()
    for l in lines:
        left,right = l.split('-')
        #print(left, right)

        add_to_map(computer_map, left, right)
        add_to_map(computer_map, right, left)
    return computer_map


def get_triple_connections_from_computer_map(computer_map):
    triples = set()
    for n1, o1 in computer_map.items():
        for n2, o2 in computer_map.items():
            if n1 == n2:
                continue

            for n3, o3 in computer_map.items():
                if n1 == n3 or n2 == n3:
                    continue

                if (n1 in o2 and n1 in o3) and (n2 in o1 and n2 in o3) and (n3 in o1 and n3 in o2):
                    #print(n1,n2,n3)
                    #if n1.startswith('t') or n2.startswith('t') or n3.startswith('t'):
                    mutable_set = set()
                    mutable_set.add(n1)
                    mutable_set.add(n2)
                    mutable_set.add(n3)
                    #frozenset(temp)
                    triples.add(frozenset(mutable_set)) 
    return triples


def get_triple_connections(filename):
    computer_map = get_computer_map(filename)
    #print(computer_map)

    triples = get_triple_connections_from_computer_map(computer_map)
    return len(triples)


def solve_part1(filename):
    computer_map = get_computer_map(filename)
    #print(computer_map)

    triples = get_triple_connections_from_computer_map(computer_map)

    ans = 0
    for t in triples:
        n1,n2,n3 = t
        if n1.startswith('t') or n2.startswith('t') or n3.startswith('t'):
            ans += 1

    return ans


def solve_part2(filename):
    computer_map = get_computer_map(filename)

    #print(computer_map)

    exclusions = set()
    for n1,v1 in computer_map.items():
        for n2, v2 in computer_map.items():
            if n1 == n2:
                continue

            for n3, v3 in computer_map.items():
                if n1 == n3 or n2 == n3:
                    continue

                #if n1 not in v3 or n2 not in v3:
                #    continue

                intersection = v1.intersection(v2).intersection(v3)
                if len(intersection) == 2:
                    #print(f"DEBUG: n1={n1} n2={n2} n3={n3} interection={intersection}")
                    exclusions.add(n1)
                    exclusions.add(n2)
              
              
    keys = set(computer_map.keys())
    remainder = sorted(keys.difference(exclusions))
    print(f"DEBUG: remainder={remainder} keys={keys} exclusions={exclusions}")
    
    return ','.join(map(str, remainder))