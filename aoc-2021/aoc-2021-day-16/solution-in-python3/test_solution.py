import pytest

# Local
import solution as solution

@pytest.mark.parametrize(
    "hex_str,expected",
    [
        pytest.param("D2FE28", "110100101111111000101000"),
        pytest.param("38006F45291200", "00111000000000000110111101000101001010010001001000000000"),
        pytest.param("EE00D40C823060", "11101110000000001101010000001100100000100011000001100000"), 
    ],    
)
def test_hex_to_binary(hex_str, expected):
    map = solution.create_hex_to_binary_map()
    assert solution.hex_to_binary(map, hex_str) == expected

@pytest.mark.parametrize(
    "hex_string, expected_version, expected_type_id, expected_literal_value_as_binary_string, expected_literal_value",
    [
        pytest.param("D2FE28", 6, 4, "011111100101", 2021),
        pytest.param("D2FEA84", 6, 4, "0111111001010001", 32337), 
        pytest.param("114", 0, 4, "1010", 10), # 000 100 0 1010 0
        pytest.param("B16", 5, 4, "1011", 11), # 101 100 0 1011 0
        pytest.param("118", 0, 4, "1100", 12), # 000 100 0 1100 0
        pytest.param("71A", 3, 4, "1101", 13), # 011 100 0 1101 0
    ],    
)
def test_literal_packet(hex_string, expected_version, expected_type_id, expected_literal_value_as_binary_string, expected_literal_value):
    # When: packet created from binary srting
    packet = solution.parse_hex_string_to_packet(hex_string)
    assert type(packet) is solution.PacketLiteral

    # Then: packet header is as expected
    header = packet.get_header()
    assert type(header) is solution.PacketHeader
    assert header.is_literal() == True
    assert header.is_operator() == False
    assert header.get_version() == expected_version
    assert header.get_type_id() == expected_type_id
    assert header.get_size() == 6

    # Then: packet body has expected literal attributes
    assert packet.get_body() == expected_literal_value_as_binary_string
    assert packet.get_value() == expected_literal_value
    assert packet.get_size() == 6 + len(expected_literal_value_as_binary_string)


@pytest.mark.parametrize(
    "hex_string, expected_version, expected_type_id, expected_length_type_id, expected_sub_packet_literals",
    [
        pytest.param("38006F45291200", 1, 6, 0, [10,20]),
        pytest.param("EE00D40C823060", 7, 3, 1, [1,2,3])
    ],    
)
def test_operator_packet_using_hex(hex_string, expected_version, expected_type_id, expected_length_type_id, expected_sub_packet_literals):
    map = solution.create_hex_to_binary_map()
    binary_string = solution.hex_to_binary(map, hex_string)
    return test_operator_packet_using_binary(binary_string, expected_version, expected_type_id, expected_length_type_id, expected_sub_packet_literals)


@pytest.mark.parametrize(
    "binary_string, expected_version, expected_type_id, expected_length_type_id, expected_sub_packet_literals",
    [
        pytest.param("001000100000000010000100011000111000110100", 1, 0, 1, [12,13]),
        pytest.param("00000000000000000101100001000101010110001011", 0, 0, 0, [10, 11])
    ],    
)
def test_operator_packet_using_binary(binary_string, expected_version, expected_type_id, expected_length_type_id, expected_sub_packet_literals):
    # When: packet created from binary srting
    packet = solution.parse_binary_string_to_packet(binary_string)
    assert type(packet) is solution.PacketOperator
    header = packet.get_header()

    # Then: packet header type is as expected
    assert type(header) is solution.PacketHeader
    assert header.is_operator() == True
    assert header.is_literal() == False
    assert header.get_version() == expected_version
    assert header.get_type_id() == expected_type_id
    assert header.get_size() == 6

    # Then: packet has expected operater attributes
    assert packet.get_operator_type_id() == expected_length_type_id
    assert packet.get_number_of_sub_packets() == len(expected_sub_packet_literals)
    #assert packet.get_sub_packet_literals() == expected_sub_packet_literals 
    for sp in packet.get_sub_packets():
        assert type(sp) is solution.PacketLiteral
        assert sp.get_value() in expected_sub_packet_literals


def test_problematic_packet():
    map = solution.create_hex_to_binary_map()
    binary_string = solution.hex_to_binary(map, "620080001611562C8802118E34")

    assert binary_string == "01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100"

    packet = solution.parse_binary_string_to_packet(binary_string)
    assert type(packet) is solution.PacketOperator

    sub_packets =  packet.get_sub_packets()
    assert len(sub_packets) == 2
    for sp in sub_packets:
        print(f"DEBUG: sp={sp}")
        assert type(sp) is solution.PacketLiteral



@pytest.mark.parametrize(
    "hex_string,expected",
    [
        pytest.param("8A004A801A8002F478", 16), # operator packet (version 4) which contains an operator packet (version 1) which contains an operator packet (version 5) which contains a literal value (version 6)
        #pytest.param("620080001611562C8802118E34", 12), # operator packet (version 3) which contains two sub-packets; each sub-packet is an operator packet that contains two literal values
        #pytest.param("C0015000016115A2E0802F182340",23), # has the same structure as the previous example, but the outermost packet uses a different length type ID
        #pytest.param("A0016C880162017C3686B18A3D4780", 31), # operator packet that contains an operator packet that contains an operator packet that contains five literal values
    ],    
)
def test_version_sum(hex_string, expected):
    assert solution.get_version_sum(hex_string) == expected