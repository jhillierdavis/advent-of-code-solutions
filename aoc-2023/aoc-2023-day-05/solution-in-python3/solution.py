from helpers import fileutils

from collections import defaultdict

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

    seed_to_soil_map = MyDefaultDict(int)  
    soil_to_fertilizer_map = MyDefaultDict(int)
    fertilizer_to_water_map = MyDefaultDict(int)
    water_to_light_map = MyDefaultDict(int)
    light_to_temperature_map = MyDefaultDict(int)
    temperature_to_humidity_map = MyDefaultDict(int)
    humidity_to_location_map = MyDefaultDict(int)
    

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
        for i in range(int(values[2])):
            map[int(values[1])+i] = int(values[0])+i


    soil = seed_to_soil_map[seed]    
    print(f"DEBUG: soil={soil}")

    fertilizer = soil_to_fertilizer_map[soil]    
    print(f"DEBUG: fertilizer={fertilizer}")

    water = fertilizer_to_water_map[fertilizer]
    print(f"DEBUG: water={water}")

    light = water_to_light_map[water]
    print(f"DEBUG: light={light}")

    temperature = light_to_temperature_map[light]
    print(f"DEBUG: temperature={temperature}")

    humidity = temperature_to_humidity_map[temperature]
    print(f"DEBUG: humidity={humidity}")

    location = humidity_to_location_map[humidity]
    print(f"DEBUG: location={location}")


    return location

def get_nearest_location_for_seeds_from_filename(filename):
    seed_lines = fileutils.get_lines_before_empty_from_file(filename)

    #print(f"DEBUG: seed_lines={seed_lines}")
    (s,v) = seed_lines[0].split(':')    
    seed_list = v.split()
    print(f"DEBUG: seed_list={seed_list}")


    map_lines = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: {map_lines}={map_lines}")

    seed_to_soil_map = MyDefaultDict(int)  
    soil_to_fertilizer_map = MyDefaultDict(int)
    fertilizer_to_water_map = MyDefaultDict(int)
    water_to_light_map = MyDefaultDict(int)
    light_to_temperature_map = MyDefaultDict(int)
    temperature_to_humidity_map = MyDefaultDict(int)
    humidity_to_location_map = MyDefaultDict(int)
    

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
        for i in range(int(values[2])):
            map[int(values[1])+i] = int(values[0])+i


    seed_to_location_map = defaultdict(int)

    for seed in seed_list:
        soil = seed_to_soil_map[int(seed)]    
        print(f"DEBUG: soil={soil}")

        fertilizer = soil_to_fertilizer_map[soil]    
        print(f"DEBUG: fertilizer={fertilizer}")

        water = fertilizer_to_water_map[fertilizer]
        print(f"DEBUG: water={water}")

        light = water_to_light_map[water]
        print(f"DEBUG: light={light}")

        temperature = light_to_temperature_map[light]
        print(f"DEBUG: temperature={temperature}")

        humidity = temperature_to_humidity_map[temperature]
        print(f"DEBUG: humidity={humidity}")

        location = humidity_to_location_map[humidity]
        print(f"DEBUG: location={location}")

        seed_to_location_map[seed] = int(location)


    return min(seed_to_location_map.values())