import pytest

import solution

input_example = "AOC-2020-Day-04_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-04_Puzzle-Input-Full.txt"

@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 2),
        pytest.param(input_full, 245),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value

@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param(2002, True),
        pytest.param(2003, False),
    ]
)
def test_is_valid_birthyear(value, expected):
    assert expected == solution.is_valid_birthyear(value)


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param('60in', True),
        pytest.param('190cm', True),
        pytest.param('190in', False),
        pytest.param('190', False),
    ]
)
def test_is_valid_height(value, expected):
    assert expected == solution.is_valid_height(value)

@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param('#123abc', True),
        pytest.param('#123abz', False),
        pytest.param('123abc', False),
    ]
)
def test_is_valid_haircolor(value, expected):
    assert expected == solution.is_valid_haircolor(value)


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param('brn', True),
        pytest.param('wat', False),
    ]
)
def test_is_valid_eyecolor(value, expected):
    assert expected == solution.is_valid_eyecolor(value)

@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param('000000001', True),
        pytest.param('0123456789', False),
    ]
)
def test_is_valid_passportid(value, expected):
    assert expected == solution.is_valid_passportid(value)


@pytest.mark.parametrize(
    "passport, expected",
    [
        pytest.param('eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926', False),
        pytest.param('iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946', False),
        pytest.param('hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277', False),
        pytest.param('hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007', False),
        pytest.param('pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f', True),
        pytest.param('eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm', True),
        pytest.param('hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022', True),
        pytest.param('iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719', True),        
    ],    
)
def test_is_valid_passport(passport, expected):
    assert expected == solution.is_valid_passport(passport)

#@pytest.mark.skip(reason="TODO")
@pytest.mark.parametrize(
    "filename, expected",
    [
        #pytest.param(input_example, 2),
        pytest.param(input_full, 133),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value   
