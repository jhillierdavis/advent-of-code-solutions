# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

"""
def process_rule_list(rule:list, rule_map:dict, idx:int=0, prefixes:list=list()):
    
    new_prefixes = list()
    for i in rule:
        if int == type(i):
            sub_prefixes = generate_valid_values(rule_map, i, prefixes)  
            for p in prefixes:
                for sp in sub_prefixes:
                    new_prefixes.append(p + sp)
        elif list == type(i):
            for l in rule:                
                sub_prefixes = process_rule_list(l, rule_map, idx, prefixes)
                for p in prefixes:
                    for sp in sub_prefixes:
                        new_prefixes.append(p + sp)
        else:
            raise Exception(f"Unexpected rule={rule}")
    logger.debug(f"process_rule_list: rile={rule} idx={idx} new_prefixes={new_prefixes}")
    return new_prefixes


def add_suffix(prefixes, suffix):
    new_values = list()
    for p in prefixes:
        new_values.append(p + suffix)
    return new_values


def generate_valid_values(rule_map:dict, idx:int=0, prefixes:list=list()):
    rule = rule_map[idx]
    logger.debug(f"generate_valid_values: idx={idx} rule={rule} prefixes={prefixes}")

    if str == type(rule):
        return add_suffix(prefixes, rule)
    
    if list == type(rule):
       return process_rule_list(rule, rule_map, idx, prefixes)

    raise Exception(f"Unexpected rule={rule}")
"""


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


def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    rule_lines = fileutils.get_lines_before_empty_from_file(filename)
    rule_map = create_rule_map_from_lines(rule_lines)

    valid_list = get_rule_values(rule_map, 0)
    valid_set = set(valid_list)
    logger.debug(f"valid_set={valid_set}")
        
    message_lines = fileutils.get_lines_after_empty_from_file(filename)

    ans = 0
    for msg in message_lines:
        if msg in valid_set:
            ans += 1
    return ans


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)
    return "TODO"



#lines = ['0: 4 1 5', '1: 2 3 | 3 2', '2: 4 4 | 5 5', '3: 4 5 | 5 4', '4: "a"', '5: "b"']
#rule_map = create_rule_map_from_lines(lines)

"""
def process_rule_steps(rule_map, idx, prefixes:set=set()):    
    values = set()
    rule_steps = rule_map[idx]
    for rs in rule_steps:
        
        if int == type(rs):
            results = process_rule_steps(rule_map, rs, values)
            for r in results:
                values.add(r)
            logger.debug(f"Rule index: rs={rs} values={values} prefixes={prefixes}")
        elif str == type(rs):                        
            if len(prefixes) > 0:
                
                for p in prefixes:
                    values.add(p + rs)
            else:
                values.add(rs)
            
            logger.debug(f"Value: rs={rs} values={values} prefixes={prefixes}")

        elif list == type(rs):
            origs = values.copy()
            for l in rs:
                assert int == type(l)
                results = process_rule_steps(rule_map, l, origs)
                for r in results:
                    values.add(r)
    return values
"""

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
    

def get_rule_values(rule_map, idx):
    rule = rule_map[idx]

    rule_values = list()

    if is_leaf_rule(rule):
        rule_values.append(rule)
    elif is_index_rule(rule):        
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
    else:
        
        for rule_option in rule:
            option_values = []
            for entry in rule_option:
                sub_values = get_rule_values(rule_map, entry)
                
                if len(option_values) == 0:
                    option_values = sub_values.copy()
                else:
                    combined = []
                    for sv in sub_values:
                        for op in option_values:
                            combined.append(op + sv)
                    option_values = combined.copy()
            rule_values += option_values

    return rule_values


#values = get_rule_values(rule_map, 0)
#logger.debug(f"values={values}")


#valid_values = generate_valid_values(rule_map, 0)
#valid_set = set(valid_values)
#logger.debug(f"valid_set={valid_set}")