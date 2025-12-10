# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def process_config(cfg):
    vals = cfg.split()
    indicators = vals[0]
    logger.debug(f"indicators={indicators}")
    wirings = vals[1:-1]
    logger.debug(f"wirings={wirings}")
    joltages = vals[-1]
    logger.debug(f"joltages={joltages}")

    return indicators, wirings, joltages


def toggle_light(status):
    if status == '.':
        return '#'
    if status == '#':
        return '.'
    raise Exception(f"Unrecognised status={status}!")


def get_pressed_count(press_map):
    total_count = 0
    for v in press_map.values():
        total_count += v
    return total_count

def get_unpressed_count(press_map):
    total_count = 0
    for v in press_map.values():
        if v == 0:
            total_count += 1
    return total_count


def press_buttons_at_most_once(button_press_idx, button_map, current_state, target_state, press_map, totals):
    new_state = current_state.copy()
    press_map = press_map.copy()

    wiring = button_map[button_press_idx]
    for wi in wiring:
        status = current_state[wi]
        new_state[wi] = toggle_light(status)

    press_map[button_press_idx] += 1
    #logger.debug(f"button_press_idx={button_press_idx} press_map={press_map} new_state={new_state} target_state={target_state}")

    # Abort if already found solution with same or fewer presses
    total_count = get_pressed_count(press_map)
    if len(totals) > 0:
        for t in totals:
            if total_count >= t:
                return

    if new_state == target_state:        
        logger.debug(f"Matched: total_count={total_count} press_map={press_map} new_state={new_state} target_state={target_state}")   
        totals.add(total_count)
        return # Matched
    
    for bk in button_map.keys():
        if press_map[bk] == 0: # Unpressed
            press_buttons_at_most_once(bk, button_map, new_state, target_state, press_map, totals)


def calculate_fewest_button_presses_for_indicators(cfg):   
    indicators, wirings, _ = process_config(cfg)

    i_size = len(indicators) - 2
    current_lights = list()

    for _ in range(i_size):
        current_lights.append('.')
    logger.debug(f"current_lights={current_lights}")

    target_lights = list()
    for i in range(i_size):
        target_lights.append(indicators[1+i])
    logger.debug(f"target_lights={target_lights}")

    button_map = dict()
    press_map = dict()

    for i, w in enumerate(wirings):
        wl = list()
        vals = w[1:-1].split(',')
        for v in vals:
            idx = int(v)
            if idx < len(target_lights):
                wl.append(idx)
        button_map[i] = wl
        press_map[i] = 0

    logger.debug(f"button_map={button_map}")
    logger.debug(f"press_map={press_map}")

    totals = set()

    for bk in button_map.keys():
        press_buttons_at_most_once(bk, button_map, current_lights, target_lights, press_map, totals)

    logger.debug(f"totals={totals}")
    return min(totals)


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)
    ans = 0
    for l in lines:
        ans += calculate_fewest_button_presses_for_indicators(l)
    return ans

def determine_new_joltage_state(button_press_idx, button_map, new_state):
    wiring = button_map[button_press_idx]
    for wi in wiring:
        new_state[wi] += 1
    return new_state


def press_joltage_buttons(button_press_idx, button_map, current_state, target_state, press_map, totals):
    new_state = current_state.copy()
    press_map = press_map.copy()

    """
    wiring = button_map[button_press_idx]
    for wi in wiring:
        new_state[wi] += 1
    """
    #new_state = determine_new_joltage_state(button_press_idx, button_map, new_state)
    #hashed_button_map = make_hashable(button_map)
    #hashed_new_state = make_hashable(new_state)
    #new_state = determine_new_joltage_state_cachable(button_press_idx, hashed_button_map, hashed_new_state)
    new_state = determine_new_joltage_state(button_press_idx, button_map, new_state)

    press_map[button_press_idx] += 1
    #logger.debug(f"button_press_idx={button_press_idx} press_map={press_map} new_state={new_state} target_state={target_state}")

    # Abort if already found solution with same or fewer presses
    total_count = get_pressed_count(press_map)
    if len(totals) > 0:
        for t in totals:
            if total_count >= t:
                return

    if new_state == target_state:        
        logger.debug(f"Matched: total_count={total_count} press_map={press_map} new_state={new_state} target_state={target_state}")   
        totals.add(total_count)
        return # Matched
    
    for i, nv in enumerate(new_state):
        if nv > target_state[i]:
            return
    
    for bk in button_map.keys():
        press_joltage_buttons(bk, button_map, new_state, target_state, press_map, totals)

    # Clean-up
    press_map = None
    target_state = None


def calculate_fewest_button_presses_for_joltages(cfg):
    _, wirings, joltages = process_config(cfg)
    
    current_joltages = list()
    logger.debug(f"current_joltages={current_joltages}")

    target_joltages = [int(j) for j in joltages[1:-1].split(',')]
    logger.debug(f"target_joltages={target_joltages}")

    current_joltages = [0 for _ in target_joltages]
    logger.debug(f"current_joltages={current_joltages}")

    button_map = dict()
    press_map = dict()

    for i, w in enumerate(wirings):
        wl = list()
        vals = w[1:-1].split(',')
        for v in vals:
            idx = int(v)
            if idx < len(target_joltages):
                wl.append(idx)
        button_map[i] = wl
        press_map[i] = 0

    logger.debug(f"button_map={button_map}")
    logger.debug(f"press_map={press_map}")

    """
    totals = set()

    for bk in button_map.keys():
        press_joltage_buttons(bk, button_map, current_joltages, target_joltages, press_map, totals)
    """

    totals = bfs(button_map, target_joltages, current_joltages, press_map)
    logger.debug(f"totals={totals}")


    return min(totals)


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")

    lines = fileutils.get_file_lines_from(filename)
    ans = 0
    for i, l in enumerate(lines):
        if i > 3:
            break

        ans += calculate_fewest_button_presses_for_joltages(l)
    return ans


from collections import deque

def process(button_press_idx, button_map, current_state, target_state, press_map, totals):
    new_state = current_state.copy()
    press_map = press_map.copy()

    new_state = determine_new_joltage_state(button_press_idx, button_map, new_state)

    press_map[button_press_idx] += 1

    # Abort if already found solution with same or fewer presses
    total_count = get_pressed_count(press_map)
    if len(totals) > 0:
        for t in totals:
            if total_count >= t:
                return None, None

    if new_state == target_state:        
        logger.debug(f"Matched: total_count={total_count} press_map={press_map} new_state={new_state} target_state={target_state}")   
        totals.add(total_count)
        return None, None
    
    # Exceeded target
    for i, nv in enumerate(new_state):
        if nv > target_state[i]:
            return None, None
    
    #for bk in button_map.keys():
    #    press_joltage_buttons(bk, button_map, new_state, target_state, press_map, totals)

    return new_state, press_map


def bfs(button_map, target_joltages, current_joltages, press_map):
    totals = set()

    # Step 1: Initialize queue and visited set
    queue = deque()
    for bk in button_map.keys():
        node = (bk, current_joltages, press_map)
        queue.append(node)

    # Step 2: Loop until queue is empty
    while queue:
        # Step 3: Dequeue a node
        node = queue.pop()    
        button_press_idx, current_joltages, press_map = node
        
        current_joltages, press_map = process(button_press_idx, button_map, current_joltages, target_joltages, press_map, totals)
        if current_joltages:
            for bk in button_map.keys():
                node = (bk, current_joltages, press_map)
                queue.append(node)
            
    return totals
