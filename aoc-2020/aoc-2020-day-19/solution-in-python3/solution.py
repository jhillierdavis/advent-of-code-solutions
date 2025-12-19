# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def values_to_lists(values:str):
    result = list()
    if ' | ' in values:
        parts = values.split(' | ')
        for p in parts:
            result.append(values_to_lists(p))
    else:
        parts = values.split(' ')
        for p in parts:
            result.append(int(p))
    return result


def create_rule_map_from_lines(lines:list[str]) -> dict[int,str]:
    rule_map = dict()
    for l in lines:
        parts = l.split(": ")
        idx = int(parts[0])
        if '"' in parts[1]:
            rule_map[idx] = parts[1][1:-1]
        else:    
            rule_map[idx] = values_to_lists(parts[1])
    logger.debug(f"rule_map={rule_map}")
    return rule_map


def is_valid_message(rule_map:dict, message:str) -> bool:
    valid_list = get_rule_values(rule_map, 0)
    valid_set = set(valid_list)
    logger.debug(f"valid_set={valid_set}")

    return message in valid_set


def is_leaf_rule(rule):    
    is_leaf = str == type(rule) and len(rule) == 1
    #logger.debug(f"is_leaf_rule: rule={rule} is_leaf={is_leaf}")
    return is_leaf
    

def is_rule_index(rule_entry):
    return int == type(rule_entry)


def is_index_rule(rule):
    if int == type(rule[0]):
        return True
    return False


def get_index_rule_values(rule_map, rule):
    rule_values = list()

    for entry in rule:
        sub_values = get_rule_values(rule_map, entry)
        
        if len(rule_values) == 0:
            rule_values = sub_values.copy()
        else:
            combined = []
            for sv in sub_values:
                for rv in rule_values:
                    combined.append(rv + sv)
            rule_values = combined.copy()   
    return rule_values


def get_rule_values(rule_map, idx):
    rule = rule_map[idx]

    rule_values = list()

    if is_leaf_rule(rule):
        rule_values.append(rule)
    elif is_index_rule(rule):        
        rule_values = get_index_rule_values(rule_map, rule) 
    else: # list of options
        for rule_option in rule:
            rule_values += get_index_rule_values(rule_map, rule_option) 

    return rule_values


def determine_valid_message_count_from_file(filename:str, apply_looping_rules:bool=False) -> int:
    rule_lines = fileutils.get_lines_before_empty_from_file(filename)
    rule_map = create_rule_map_from_lines(rule_lines)

    valid_list = get_rule_values(rule_map, 0)
    valid_set = set(valid_list)
    #logger.debug(f"valid_set={valid_set}")
        
    message_lines = fileutils.get_lines_after_empty_from_file(filename)

    ans = 0
    for msg in message_lines:
        if msg in valid_set:
            ans += 1
    return ans    


def solve_part1(filename):
    return determine_valid_message_count_from_file(filename)


def solve_part2(filename):
    return determine_valid_message_count_from_file(filename)