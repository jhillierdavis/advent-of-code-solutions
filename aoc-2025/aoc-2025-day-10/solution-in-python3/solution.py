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


def calculate_fewest_button_presses(cfg):
   
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
        ans += calculate_fewest_button_presses(l)
    return ans


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)
    return "TODO"
