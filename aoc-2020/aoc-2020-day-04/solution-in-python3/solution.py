from helpers import fileutils

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


def solve_part1(filename):
    lines = fileutils.get_contiguous_non_empty_lines_from(filename)
    #lines = fileutils.get_file_lines_from(filename)

    valid_count = 0
    for l in lines:
        print(f"DEBUG: {l}")
        str_passport = ' '.join(l)
        if all(ele in str_passport for ele in ['byr:', 'iyr:', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            valid_count += 1

    return valid_count


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

def solve_part2(filename):
    return -1