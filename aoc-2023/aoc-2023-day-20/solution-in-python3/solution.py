from collections import defaultdict, deque
from abc import ABC, abstractmethod
import math

from helpers import fileutils

class Module(ABC):
    def __init__(self, name:str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    @abstractmethod    
    def process(module_name:str, pulse:int) -> int:
        return 0


class FlipflopModule(Module):

    def __init__(self, name):
        super().__init__(name)  
        self.is_on:bool = False
        #print(f"DEBUG: [FlipflopModule] Constructor: name={name}")

    def process(self, module_name:str, pulse:int) -> int:
        if pulse == 0:
            self.is_on = False if self.is_on else True # Toggle
            if self.is_on:
                return 1
            else:
                return 0        
        return None

class ConjunctionModule(Module):

    def __init__(self, name, keys):
        super().__init__(name)  
        self.last_pulse_map = defaultdict(int)
        for k in keys:
            if name != k:
                self.last_pulse_map[k] = 0
        #print(f"DEBUG: [ConjunctionModule] Constructor: name={name} keys={keys} last_pulse_map={self.last_pulse_map}")

    def process(self, module_name:str, pulse:int) -> int:
        self.last_pulse_map[module_name] = pulse
        #print(f"DEBUG: Process self.last_pulse_map={self.last_pulse_map} for self.name={self.name} module_name={module_name}")
        if all(self.last_pulse_map.values()): # All High?
            return 0
        return 1


def get_module_config_map_from(lines):
    module_config_map = {}

    for l in lines:
        m, _ = l.split(" -> ")
        module_config_map[m] = None

    # Fix annoying map value naming
    for l in lines:
        values = []
        m, e = l.split(" -> ")
        for item in e.strip().split(", "):
            flipflop = '%' + item
            conjunction = '&' + item

            if item in module_config_map:
                values.append(item)
            elif flipflop in module_config_map:
                values.append(flipflop)
            elif conjunction in module_config_map:
                values.append(conjunction)                
            else:
                values.append(item)
                module_config_map[item] = []
        module_config_map[m] = values
    return module_config_map

def get_keys_with_values_including(module_config_map, target):
    matches = []
    for k in module_config_map.keys():
        if not k == target and target in module_config_map[k]:
            matches.append(k)
    return matches

def get_module_map_from_config(module_config_map):
    module_map = {}
    for k in module_config_map.keys():
        if k.startswith('%'):
            module_map[k] = FlipflopModule(k)
        if k.startswith('&'):
            matches = get_keys_with_values_including(module_config_map, k)
            module_map[k] = ConjunctionModule(k, matches)
    return module_map

def solve_part1(filename, loops=1):
    lines = fileutils.get_file_lines(filename)
    module_config_map = get_module_config_map_from(lines)
    #print(f"DEBUG: module_config_map={module_config_map}")

    module_map = get_module_map_from_config(module_config_map)
    #print(f"DEBUG: module_map={module_map}")
    #print()

    low_pulse_count = 0 
    high_pulse_count = 0
    for _ in range(loops):
        #print()
        queue_to_process = deque()
        initial_state = ('button', 'broadcaster', 0)
        low_pulse_count += 1
        queue_to_process.append(initial_state)

        while(queue_to_process):
            
            current, destination, pulse = queue_to_process.popleft()

            #print(f"DEBUG: current={current} destination={destination} pulse={pulse}")

            #print(f"DEBUG: {current} {pulse} -> {destination}")

            children = module_config_map[destination]
            for child in children:
                #print(f"DEBUG: {destination} {pulse} -> {child}")
                if pulse == 0:
                    low_pulse_count += 1
                else:
                    high_pulse_count += 1

                if child.startswith('%') or child.startswith('&'):
                    module = module_map[child]
                    updated_pulse = module.process(destination, pulse)
                    if None != updated_pulse:
                        queue_to_process.append((destination, child, updated_pulse))
                else:
                    queue_to_process.append((destination, child, pulse))
    #print()
    #print(f"DEBUG: low_pulse_count={low_pulse_count} high_pulse_count={high_pulse_count} loops={loops}")
    return low_pulse_count * high_pulse_count


def get_prior_conjuctions(module_config_map, target):
    values = []
    for k, v in module_config_map.items():
        if target in v:
            values.append(k)
    if len(values) == 1:
        return get_prior_conjuctions(module_config_map, values[0])
    return values

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    module_config_map = get_module_config_map_from(lines)
    #print(f"DEBUG: module_config_map={module_config_map}")

    module_map = get_module_map_from_config(module_config_map)
    #print(f"DEBUG: module_map={module_map}")
    #print()

    values = get_prior_conjuctions(module_config_map, 'rx')            
    #print(f"DEBUG: values={values}")

    conjuction_to_steps_map = defaultdict(int)
    for k in values:
        conjuction_to_steps_map[k] == 0
    
    press_count  = 0
    for _ in range(100000):
        press_count += 1
        queue_to_process = deque()
        initial_state = ('button', 'broadcaster', 0)
        queue_to_process.append(initial_state)

        while(queue_to_process):
            
            current, destination, pulse = queue_to_process.popleft()

            children = module_config_map[destination]
            for child in children:
                if child.startswith('%') or child.startswith('&'):
                    module = module_map[child]
                    updated_pulse = module.process(destination, pulse)
                    if (child in conjuction_to_steps_map.keys()) and updated_pulse == 1:                        
                        if conjuction_to_steps_map[child] == 0:
                            #print(f"DEBUG: press_count={press_count} child={child} updated_pulse={updated_pulse}")
                            conjuction_to_steps_map[child] = press_count
                    if None != updated_pulse:
                        queue_to_process.append((destination, child, updated_pulse))
                else:
                    queue_to_process.append((destination, child, pulse))
    
    return math.lcm(*conjuction_to_steps_map.values())