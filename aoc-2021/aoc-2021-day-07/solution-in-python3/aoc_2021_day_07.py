from collections import defaultdict

def calcuate_cost_to_align_at_position(positions, target_position, is_compound_cost = False):
    cost = 0
    for position in positions:
        diff = 0
        if position > target_position:
            diff = position - target_position
        elif position < target_position:
            diff = target_position - position
        if is_compound_cost:
            cost += sum(range(0, 1 + diff))
        else:
            cost += diff
    
    return cost

def calculate_least_cost(positions, is_compound_cost = False):
    map = defaultdict(int)
    for position in range(max(positions)):
        map[position] = calcuate_cost_to_align_at_position(positions, position, is_compound_cost)

    #print(f"DEBUG: map={map}")
    return min(map.values())


