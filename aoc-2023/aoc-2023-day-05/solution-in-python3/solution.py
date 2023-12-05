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
    seed_lines = fileutils.get_lines_before_empty_from_file(filename)

    #print(f"DEBUG: seed_lines={seed_lines}")
    (s,v) = seed_lines[0].split(':')    
    seed_list = v.split()
    #print(f"DEBUG: seed_list={seed_list}")


    map_lines = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: {map_lines}={map_lines}")

    seed_to_soil_map = AdjusterMap()
    soil_to_fertilizer_map = AdjusterMap()
    fertilizer_to_water_map = AdjusterMap()
    water_to_light_map = AdjusterMap()
    light_to_temperature_map = AdjusterMap()
    temperature_to_humidity_map = AdjusterMap()
    humidity_to_location_map = AdjusterMap()
    

    map = None
    for l in map_lines:
        values = l.split()

        if values[0] == 'seed-to-soil':
            map = seed_to_soil_map
            continue

        if values[0] == 'soil-to-fertilizer':
            map = soil_to_fertilizer_map
            continue

        if values[0] == 'fertilizer-to-water':
            map = fertilizer_to_water_map
            continue

        if values[0] == 'water-to-light':
            map = water_to_light_map
            continue

        if values[0] == 'light-to-temperature':
            map = light_to_temperature_map
            continue

        if values[0] == 'temperature-to-humidity':
            map = temperature_to_humidity_map
            continue

        if values[0] == 'humidity-to-location':
            map = humidity_to_location_map
            continue

        values = l.split()
        #print(f"DEBUG: values={values}")
        map.add_adjuster(int(values[0]),int(values[1]),int(values[2]))


    soil = seed_to_soil_map.get_value(seed)
    #print(f"DEBUG: soil={soil}")

    fertilizer = soil_to_fertilizer_map.get_value(soil)
    #print(f"DEBUG: fertilizer={fertilizer}")

    water = fertilizer_to_water_map.get_value(fertilizer)
    #print(f"DEBUG: water={water}")

    light = water_to_light_map.get_value(water)
    #print(f"DEBUG: light={light}")

    temperature = light_to_temperature_map.get_value(light)
    #print(f"DEBUG: temperature={temperature}")

    humidity = temperature_to_humidity_map.get_value(temperature)
    #print(f"DEBUG: humidity={humidity}")

    location = humidity_to_location_map.get_value(humidity)
    #print(f"DEBUG: location={location}")


    return location

def get_nearest_location_for_seeds_from_filename(filename):
    seed_list = get_seed_list_from_filename(filename)

    map_lines = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: {map_lines}={map_lines}")

    seed_to_soil_map = AdjusterMap()
    soil_to_fertilizer_map = AdjusterMap()
    fertilizer_to_water_map = AdjusterMap()
    water_to_light_map = AdjusterMap()
    light_to_temperature_map = AdjusterMap()
    temperature_to_humidity_map = AdjusterMap()
    humidity_to_location_map = AdjusterMap()
    
    

    map = None
    for l in map_lines:
        values = l.split()

        if values[0] == 'seed-to-soil':
            map = seed_to_soil_map
            continue

        if values[0] == 'soil-to-fertilizer':
            map = soil_to_fertilizer_map
            continue

        if values[0] == 'fertilizer-to-water':
            map = fertilizer_to_water_map
            continue

        if values[0] == 'water-to-light':
            map = water_to_light_map
            continue

        if values[0] == 'light-to-temperature':
            map = light_to_temperature_map
            continue

        if values[0] == 'temperature-to-humidity':
            map = temperature_to_humidity_map
            continue

        if values[0] == 'humidity-to-location':
            map = humidity_to_location_map
            continue

        values = l.split()
        #print(f"DEBUG: values={values}")
        #for i in range(int(values[2])):
        #    map[int(values[1])+i] = int(values[0])+i
        map.add_adjuster(int(values[0]),int(values[1]),int(values[2]))


    seed_to_location_map = defaultdict(int)

    for seed in seed_list:
        soil = seed_to_soil_map.get_value(int(seed))
        #print(f"DEBUG: soil={soil}")

        fertilizer = soil_to_fertilizer_map.get_value(soil)
        #print(f"DEBUG: fertilizer={fertilizer}")

        water = fertilizer_to_water_map.get_value(fertilizer)
        #print(f"DEBUG: water={water}")

        light = water_to_light_map.get_value(water)
        #print(f"DEBUG: light={light}")

        temperature = light_to_temperature_map.get_value(light)
        #print(f"DEBUG: temperature={temperature}")

        humidity = temperature_to_humidity_map.get_value(temperature)
        #print(f"DEBUG: humidity={humidity}")

        location = humidity_to_location_map.get_value(humidity)
        #print(f"DEBUG: location={location}")

        seed_to_location_map[seed] = int(location)


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

    map_lines = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: {map_lines}={map_lines}")

    seed_to_soil_map = AdjusterMap()
    soil_to_fertilizer_map = AdjusterMap()
    fertilizer_to_water_map = AdjusterMap()
    water_to_light_map = AdjusterMap()
    light_to_temperature_map = AdjusterMap()
    temperature_to_humidity_map = AdjusterMap()
    humidity_to_location_map = AdjusterMap()
    
    

    map = None
    for l in map_lines:
        values = l.split()

        if values[0] == 'seed-to-soil':
            map = seed_to_soil_map
            continue

        if values[0] == 'soil-to-fertilizer':
            map = soil_to_fertilizer_map
            continue

        if values[0] == 'fertilizer-to-water':
            map = fertilizer_to_water_map
            continue

        if values[0] == 'water-to-light':
            map = water_to_light_map
            continue

        if values[0] == 'light-to-temperature':
            map = light_to_temperature_map
            continue

        if values[0] == 'temperature-to-humidity':
            map = temperature_to_humidity_map
            continue

        if values[0] == 'humidity-to-location':
            map = humidity_to_location_map
            continue

        values = l.split()
        #print(f"DEBUG: values={values}")
        #for i in range(int(values[2])):
        #    map[int(values[1])+i] = int(values[0])+i
        map.add_adjuster(int(values[0]),int(values[1]),int(values[2]))


    seed_to_location_map = defaultdict(int)

    for seed in seed_list:
        soil = seed_to_soil_map.get_value(int(seed))
        #print(f"DEBUG: soil={soil}")

        fertilizer = soil_to_fertilizer_map.get_value(soil)
        #print(f"DEBUG: fertilizer={fertilizer}")

        water = fertilizer_to_water_map.get_value(fertilizer)
        #print(f"DEBUG: water={water}")

        light = water_to_light_map.get_value(water)
        #print(f"DEBUG: light={light}")

        temperature = light_to_temperature_map.get_value(light)
        #print(f"DEBUG: temperature={temperature}")

        humidity = temperature_to_humidity_map.get_value(temperature)
        #print(f"DEBUG: humidity={humidity}")

        location = humidity_to_location_map.get_value(humidity)
        #print(f"DEBUG: location={location}")

        seed_to_location_map[seed] = int(location)


    return min(seed_to_location_map.values())


