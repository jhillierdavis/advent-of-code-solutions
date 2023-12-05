from helpers import fileutils

from collections import defaultdict

class Adjuster():
    
    def __init__(self, offset, min, scope):
        self.offset = offset
        self.min = min
        self.scope = scope

    def contains_key(self, key):
        return key >= self.min and key < self.min + self.scope
    
    def get_value(self, key):
        if not self.contains_key(key):
            raise Exception("Does not contain key={key}!")
        return self.offset + (key - self.min)

class AdjusterMap():

    def __init__(self):
        self.adjuster_list = []

    def add_adjuster(self, offset, min, scope):
        adjuster = Adjuster(offset, min, scope)
        self.adjuster_list.append(adjuster)

    def get_value(self, key):
        for adjuster in self.adjuster_list:
            if adjuster.contains_key(key):
                return adjuster.get_value(key)
        return key



class MyDefaultDict(defaultdict):
    def __missing__(self, key):
        return key

def get_location_for_seed_from_filename(filename, seed):
    map_of_maps = get_map_of_maps_from_filename(filename)
    seed_to_location_map = get_seed_to_location_map_from_seed_list(map_of_maps, [seed])
    return seed_to_location_map[seed]

def get_map_of_maps_from_filename(filename):
    map_lines = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: {map_lines}={map_lines}")

    seed_to_soil_map = AdjusterMap()
    soil_to_fertilizer_map = AdjusterMap()
    fertilizer_to_water_map = AdjusterMap()
    water_to_light_map = AdjusterMap()
    light_to_temperature_map = AdjusterMap()
    temperature_to_humidity_map = AdjusterMap()
    humidity_to_location_map = AdjusterMap()
    
    map_of_maps = {}

    map = None
    for l in map_lines:
        values = l.split()

        

        if values[0] == 'seed-to-soil':
            map = seed_to_soil_map
            map_of_maps[values[0]] = map
            continue

        if values[0] == 'soil-to-fertilizer':
            map = soil_to_fertilizer_map
            map_of_maps[values[0]] = map
            continue

        if values[0] == 'fertilizer-to-water':
            map = fertilizer_to_water_map
            map_of_maps[values[0]] = map
            continue

        if values[0] == 'water-to-light':
            map = water_to_light_map
            map_of_maps[values[0]] = map
            continue

        if values[0] == 'light-to-temperature':
            map = light_to_temperature_map
            map_of_maps[values[0]] = map
            continue

        if values[0] == 'temperature-to-humidity':
            map = temperature_to_humidity_map
            map_of_maps[values[0]] = map
            continue

        if values[0] == 'humidity-to-location':
            map = humidity_to_location_map
            map_of_maps[values[0]] = map
            continue

        values = l.split()
        #print(f"DEBUG: values={values}")
        #for i in range(int(values[2])):
        #    map[int(values[1])+i] = int(values[0])+i
        map.add_adjuster(int(values[0]),int(values[1]),int(values[2]))
    
    return map_of_maps

def get_seed_to_location_map_from_seed_list(map_of_maps, seed_list):
    seed_to_location_map = defaultdict(int)

    for seed in seed_list:
        soil = map_of_maps['seed-to-soil'].get_value(int(seed))
        #print(f"DEBUG: soil={soil}")

        fertilizer = map_of_maps['soil-to-fertilizer'].get_value(soil)
        #print(f"DEBUG: fertilizer={fertilizer}")

        water = map_of_maps['fertilizer-to-water'].get_value(fertilizer)
        #print(f"DEBUG: water={water}")

        light = map_of_maps['water-to-light'].get_value(water)
        #print(f"DEBUG: light={light}")

        temperature = map_of_maps['light-to-temperature'].get_value(light)
        #print(f"DEBUG: temperature={temperature}")

        humidity = map_of_maps['temperature-to-humidity'].get_value(temperature)
        #print(f"DEBUG: humidity={humidity}")

        location = map_of_maps['humidity-to-location'].get_value(humidity)
        #print(f"DEBUG: location={location}")

        seed_to_location_map[seed] = int(location)

    return seed_to_location_map


def get_nearest_location_for_seeds_from_filename(filename):
    seed_list = get_seed_list_from_filename(filename)
    map_of_maps = get_map_of_maps_from_filename(filename)
    seed_to_location_map = get_seed_to_location_map_from_seed_list(map_of_maps, seed_list)
    return min(seed_to_location_map.values())

def get_seed_list_from_filename(filename):
    seed_lines = fileutils.get_lines_before_empty_from_file(filename)

    #print(f"DEBUG: seed_lines={seed_lines}")
    (s,v) = seed_lines[0].split(':')    
    seed_list = list(map(int, v.split()))

    return seed_list


def get_seed_list_as_range_pairs_from_filename(filename):
    pair_list = get_seed_list_from_filename(filename)

    seed_list = []
    for i in range(0, len(pair_list), 2):
        for x in range(pair_list[i+1]):
            seed_list.append(pair_list[i] + x)
    return seed_list


def solve_part2(filename):
    seed_list = get_seed_list_as_range_pairs_from_filename(filename)
    map_of_maps = get_map_of_maps_from_filename(filename)
    seed_to_location_map = get_seed_to_location_map_from_seed_list(map_of_maps, seed_list)
    return min(seed_to_location_map.values())