import pytest


"""
def hex_to_binary(hex_string:str) -> str:
    #return format(int(hex_str, 16), "040b")
    # Convert the hexadecimal string to an integer using the base 16  
    hex_integer = int(hex_string, 16)  
    # Convert the integer to binary using the bin() function  
    binary_string = bin(hex_integer)  
    # Remove the '0b' prefix from the binary string  
    binary_string = binary_string[2:] 
    return binary_string
"""

def create_hex_to_binary_map():
    map = {}

    map['0'] = '0000'
    map['1'] = '0001'
    map['2'] = '0010'
    map['3'] = '0011'
    map['4'] = '0100'
    map['5'] = '0101'
    map['6'] = '0110'
    map['7'] = '0111'
    map['8'] = '1000'
    map['9'] = '1001'
    map['A'] = '1010'
    map['A'] = '1010'
    map['B'] = '1011'
    map['C'] = '1100'
    map['D'] = '1101'
    map['E'] = '1110'
    map['F'] = '1111'

    return map

def hex_to_binary(map, hex_string:str) -> str:
    binary_string = ""
    for i in range(len(hex_string)):
        binary_string += map[ hex_string[i] ]
    return binary_string


@pytest.mark.parametrize(
    "hex_str,expected",
    [
        pytest.param("D2FE28", "110100101111111000101000"),
        pytest.param("38006F45291200", "00111000000000000110111101000101001010010001001000000000"),
        pytest.param("EE00D40C823060", "11101110000000001101010000001100100000100011000001100000"), 
    ],    
)
def test_hex_to_binary(hex_str, expected):
    map = create_hex_to_binary_map()
    assert hex_to_binary(map, hex_str) == expected


def get_version_sum(hex_string:str) -> int:
    map = create_hex_to_binary_map()
    binary_string = hex_to_binary(map, hex_string)
    print(f"DEBUG: binary_string={binary_string}")
    return 0



@pytest.mark.parametrize(
    "hex_string,expected",
    [
        pytest.param("8A004A801A8002F478", 16),
    ],    
)
def test_version_sum(hex_string, expected):
    assert get_version_sum(hex_string) == expected