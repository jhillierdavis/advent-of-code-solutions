from helpers import fileutils

import re

"""
Passport fields:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

def get_combined_lines_from_multi_lines_from(filename):
    line_array = []
    multilines = fileutils.get_contiguous_non_empty_lines_from(filename)
    for ml_array in multilines:
        line = ' '.join(ml_array)
        line_array.append(line)

    return line_array


def solve_part1(filename):
    lines = get_combined_lines_from_multi_lines_from(filename)
    #lines = fileutils.get_file_lines_from(filename)

    valid_count = 0
    for l in lines:
        #print(f"DEBUG: {l}")
        if all(ele in l for ele in ['byr:', 'iyr:', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            valid_count += 1

    return valid_count


def is_valid_birthyear(value):
    if value < 1920 or value > 2002:
        return False
    return True


def is_valid_height(value):

    #hgt (Height) - a number followed by either cm or in:
    #If cm, the number must be at least 150 and at most 193.
    #If in, the number must be at least 59 and at most 76.    

    if value.endswith('cm'):
        value = int(value.strip('cm'))
        if value < 150 or value > 193:
            return False
        return True
    elif value.endswith('in'):
        value = int(value.strip('in'))
        if value < 59 or value > 76:
            return False
        return True
    else:
        return False

def is_valid_haircolor(value):
    pattern = re.compile(r'#[0-9a-f]{6}')
    if pattern.fullmatch(value):
        return True
    return False

def is_valid_eyecolor(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def is_valid_passportid(value):
    pattern = re.compile(r'\d{9}')
    if pattern.fullmatch(value):
        return True
    return False


"""
Passport field validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

def is_valid_passport(passport):
    fields_array = passport.split(' ')
    for field in fields_array:

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if field.startswith('byr:'):
            value = int(field.split(':')[1])
            #print(f'DEBUG: field={field} value={value}')
            if not is_valid_birthyear(value):
                return False

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if field.startswith('iyr:'):
            value = int(field.split(':')[1])
            #print(f'DEBUG: field={field} value={value}')
            if value < 2010 or value > 2020:
                return False

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if field.startswith('eyr:'):
            value = int(field.split(':')[1])
            #print(f'DEBUG: field={field} value={value}')
            if value < 2020 or value > 2030:
                return False

        #hgt (Height) - a number followed by either cm or in:
        #If cm, the number must be at least 150 and at most 193.
        #If in, the number must be at least 59 and at most 76.
        if field.startswith('hgt:'):
            value = field.split(':')[1]        
            if not is_valid_height(value):
                return False
                
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.        
        if field.startswith('hcl:'):
            value = field.split(':')[1]               
            if not is_valid_haircolor(value):
                return False

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if field.startswith('ecl:'):
            value = field.split(':')[1]   
            if not is_valid_eyecolor(value):
                return False

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if field.startswith('pid:'):
            value = field.split(':')[1]   
            if not is_valid_passportid(value):
                return False
            
    return True

def solve_part2(filename):
    lines = get_combined_lines_from_multi_lines_from(filename)
    #lines = fileutils.get_file_lines_from(filename)

    valid_count = 0
    for l in lines:
        #print(f"DEBUG: {l}")
        if all(ele in l for ele in ['byr:', 'iyr:', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            if is_valid_passport(l):
                valid_count += 1

    return valid_count