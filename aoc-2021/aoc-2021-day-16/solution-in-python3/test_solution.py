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
    "hex_string, expected_binary_string, expected_version, expected_type_id, expected_bit_length, expected_literal_value_as_binary_string, expected_literal_value",
    [
        pytest.param("D2FE28", "110100101111111000101000", 6, 4, 21, "011111100101", 2021),
        pytest.param("D2FEA84", "1101001011111110101010000100", 6, 4, 26, "0111111001010001", 32337), 
        pytest.param("114", "000100010100", 0, 4, 11, "1010", 10), # 000 100 0 1010 0
        pytest.param("B16", "101100010110", 5, 4, 11, "1011", 11), # 101 100 0 1011 0
        pytest.param("118", "000100011000", 0, 4, 11, "1100", 12), # 000 100 0 1100 0
        pytest.param("71A", "011100011010", 3, 4, 11, "1101", 13), # 011 100 0 1101 0
    ],    
)
def test_next_literal_packet(hex_string, expected_binary_string, expected_version, expected_type_id, expected_bit_length, expected_literal_value_as_binary_string, expected_literal_value):
    # When: packet created from binary srting
    binary_string = solution.hex_string_to_binary_string(hex_string)
    assert binary_string == expected_binary_string
    packet = solution.parse_binary_string_to_next_packet(binary_string)
    assert type(packet) is solution.PacketLiteral

    # Then: packet header is as expected
    header = packet.get_header()
    assert type(header) is solution.PacketHeader
    assert header.is_literal() == True
    assert header.is_operator() == False
    assert header.get_version() == expected_version
    assert header.get_type_id() == expected_type_id
    assert header.get_bit_length() == 6

    # Then: packet body has expected literal attributes
    assert packet.get_body() == expected_literal_value_as_binary_string
    assert packet.get_value() == expected_literal_value

    # And: literal packet has expected bit length
    assert packet.get_bit_length() == expected_bit_length
    

@pytest.mark.parametrize(
    "hex_string, expected_binary_string, expected_version, expected_type_id, expected_length_type_id, expected_bit_length, expected_sub_packet_literals",
    [
        pytest.param("38006F45291200", "00111000000000000110111101000101001010010001001000000000", 1, 6, 0, 49, [10,20]),
        pytest.param("EE00D40C823060", "11101110000000001101010000001100100000100011000001100000", 7, 3, 1, 51, [1,2,3]),
    ],    
)
def test_operator_packet_using_hex(hex_string, expected_binary_string, expected_version, expected_type_id, expected_length_type_id, expected_bit_length, expected_sub_packet_literals):
    binary_string = solution.hex_string_to_binary_string(hex_string)
    assert binary_string == expected_binary_string
    return test_operator_packet_using_binary(binary_string, expected_version, expected_type_id, expected_length_type_id, expected_bit_length, expected_sub_packet_literals)


@pytest.mark.parametrize(
    "binary_string, expected_version, expected_type_id, expected_length_type_id, expected_bit_length, expected_sub_packet_literals",
    [
        pytest.param("001000100000000010000100011000111000110100", 1, 0, 1, 40, [12,13]),
        pytest.param("00000000000000000101100001000101010110001011", 0, 0, 0, 44, [10, 11])
    ],    
)
def test_operator_packet_using_binary(binary_string, expected_version, expected_type_id, expected_length_type_id, expected_bit_length, expected_sub_packet_literals):
    # When: packet created from binary srting
    packet = solution.parse_binary_string_to_next_packet(binary_string)
    assert type(packet) is solution.PacketOperator
    header = packet.get_header()

    # Then: packet header type is as expected
    assert type(header) is solution.PacketHeader
    assert header.is_operator() == True
    assert header.is_literal() == False
    assert header.get_version() == expected_version
    assert header.get_type_id() == expected_type_id
    assert header.get_bit_length() == 6

    # Then: packet has expected operater attributes
    assert packet.get_operator_type_id() == expected_length_type_id
    assert packet.get_number_of_sub_packets() == len(expected_sub_packet_literals)
    assert packet.get_bit_length() == expected_bit_length
    #assert packet.get_sub_packet_literals() == expected_sub_packet_literals 
    for sp in packet.get_sub_packets():
        assert type(sp) is solution.PacketLiteral
        assert sp.get_value() in expected_sub_packet_literals

@pytest.mark.parametrize(
    "binary_string, expected_version, expected_type_id, expected_length_type_id, expected_sub_packet_literals",
    [
        pytest.param("001000100000000010000100011000111000110100", 1, 0, 1, [12,13]),
        pytest.param("00000000000000000101100001000101010110001011", 0, 0, 0, [10, 11])
    ],    
)
def test_operator_packets_using_binary(binary_string, expected_version, expected_type_id, expected_length_type_id, expected_sub_packet_literals):
    # When: packet created from binary string
    packet = solution.parse_binary_string_to_next_packet(binary_string)

    assert type(packet) is solution.PacketOperator
    header = packet.get_header()

    # Then: packet header type is as expected
    assert type(header) is solution.PacketHeader
    assert header.is_operator() == True
    assert header.is_literal() == False
    assert header.get_version() == expected_version
    assert header.get_type_id() == expected_type_id
    assert header.get_bit_length() == 6

    # Then: packet has expected operater attributes
    assert packet.get_operator_type_id() == expected_length_type_id
    assert packet.get_number_of_sub_packets() == len(expected_sub_packet_literals)
    #assert packet.get_sub_packet_literals() == expected_sub_packet_literals 
    for sp in packet.get_sub_packets():
        assert type(sp) is solution.PacketLiteral
        assert sp.get_value() in expected_sub_packet_literals



def test_problematic_packet():
    hex_string = "620080001611562C8802118E34"
    binary_string = solution.hex_string_to_binary_string(hex_string)
    assert binary_string == "01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100"

    #packet = solution.parse_binary_string_to_packet(binary_string)
    packet_list = solution.parse_binary_string_to_packet_list(binary_string)
    assert len(packet_list) == 1
    packet = packet_list[0]
    assert type(packet) is solution.PacketOperator

    sub_packets = packet.get_sub_packets()
    assert len(sub_packets) == 2
    for sp in sub_packets:
        print(f"DEBUG: sp={sp}")
        assert type(sp) is solution.PacketOperator
        for ssp in sp.get_sub_packets():
            assert type(ssp) is solution.PacketLiteral



@pytest.mark.parametrize(
    "hex_string,expected",
    [
        pytest.param("8A004A801A8002F478", 16), # operator packet (version 4) which contains an operator packet (version 1) which contains an operator packet (version 5) which contains a literal value (version 6)
        pytest.param("620080001611562C8802118E34", 12), # operator packet (version 3) which contains two sub-packets; each sub-packet is an operator packet that contains two literal values
        pytest.param("C0015000016115A2E0802F182340",23), # has the same structure as the previous example, but the outermost packet uses a different length type ID
        pytest.param("A0016C880162017C3686B18A3D4780", 31), # operator packet that contains an operator packet that contains an operator packet that contains five literal values
        pytest.param("2056FA18025A00A4F52AB13FAB6CDA779E1B2012DB003301006A35C7D882200C43289F07A5A192D200C1BC011969BA4A485E63D8FE4CC80480C00D500010F8991E23A8803104A3C425967260020E551DC01D98B5FEF33D5C044C0928053296CDAFCB8D4BDAA611F256DE7B945220080244BE59EE7D0A5D0E6545C0268A7126564732552F003194400B10031C00C002819C00B50034400A70039C009401A114009201500C00B00100D00354300254008200609000D39BB5868C01E9A649C5D9C4A8CC6016CC9B4229F3399629A0C3005E797A5040C016A00DD40010B8E508615000213112294749B8D67EC45F63A980233D8BCF1DC44FAC017914993D42C9000282CB9D4A776233B4BF361F2F9F6659CE5764EB9A3E9007ED3B7B6896C0159F9D1EE76B3FFEF4B8FCF3B88019316E51DA181802B400A8CFCC127E60935D7B10078C01F8B50B20E1803D1FA21C6F300661AC678946008C918E002A72A0F27D82DB802B239A63BAEEA9C6395D98A001A9234EA620026D1AE5CA60A900A4B335A4F815C01A800021B1AE2E4441006A0A47686AE01449CB5534929FF567B9587C6A214C6212ACBF53F9A8E7D3CFF0B136FD061401091719BC5330E5474000D887B24162013CC7EDDCDD8E5E77E53AF128B1276D0F980292DA0CD004A7798EEEC672A7A6008C953F8BD7F781ED00395317AF0726E3402100625F3D9CB18B546E2FC9C65D1C20020E4C36460392F7683004A77DB3DB00527B5A85E06F253442014A00010A8F9106108002190B61E4750004262BC7587E801674EB0CCF1025716A054AD47080467A00B864AD2D4B193E92B4B52C64F27BFB05200C165A38DDF8D5A009C9C2463030802879EB55AB8010396069C413005FC01098EDD0A63B742852402B74DF7FDFE8368037700043E2FC2C8CA00087C518990C0C015C00542726C13936392A4633D8F1802532E5801E84FDF34FCA1487D367EF9A7E50A43E90", 917)
    ],    
)
def test_version_sum(hex_string, expected): # Part 1
    #assert solution.get_version_sum(hex_string) == expected
    assert solution.parse_hex_string_to_packet_version_sum(hex_string) == expected


def evaluate_value_from_packet(packet):
    
    header = packet.get_header()
    if header.is_literal():
        return packet.get_value()
    
    values = []
    for sp in packet.get_sub_packets():
        values.append( evaluate_value_from_packet(sp))

    if header.get_type_id() == 0:
        #print(f"DEBUG: Sum ")
        result = 0
        for v in values:
            result += v
        return result
    elif header.get_type_id() == 1:
        #print(f"DEBUG: Product ")
        result = 1
        for v in values:
            result *= v   
        return result         
    elif header.get_type_id() == 2:            
        #print(f"DEBUG: Min. ")
        return min(values)
    elif header.get_type_id() == 3:
        ##print(f"DEBUG: Max. ")
        return max(values)
    elif header.get_type_id() == 4:
        return packet.get_value() # Literal
    elif header.get_type_id() == 5:
        #print(f"DEBUG: Greater than ")
        assert len(values) == 2
        return values[0] > values[1]
    elif header.get_type_id() == 6:
        #print(f"DEBUG: Less than ")
        assert len(values) == 2
        return values[0] < values[1]
    elif header.get_type_id() == 7:
        #print(f"DEBUG: Equals ")
        assert len(values) == 2
        return values[0] == values[1]

    raise Exception("Unhandled evaluation for packet: {packet}")

@pytest.mark.parametrize(
    "hex_string,expected",
    [
        pytest.param("C200B40A82", 3), # Sum
        pytest.param("04005AC33890", 54), # Product
        pytest.param("880086C3E88112", 7), # Minimum
        pytest.param("D8005AC2A8F0", 1), # Less than
        pytest.param("F600BC2D8F", 0), # Greater than
        pytest.param("9C005AC2F8F0", 0), # Equal
        pytest.param("9C0141080250320F1802104A08", 1), # 1 + 3 = 2 * 2
        pytest.param("2056FA18025A00A4F52AB13FAB6CDA779E1B2012DB003301006A35C7D882200C43289F07A5A192D200C1BC011969BA4A485E63D8FE4CC80480C00D500010F8991E23A8803104A3C425967260020E551DC01D98B5FEF33D5C044C0928053296CDAFCB8D4BDAA611F256DE7B945220080244BE59EE7D0A5D0E6545C0268A7126564732552F003194400B10031C00C002819C00B50034400A70039C009401A114009201500C00B00100D00354300254008200609000D39BB5868C01E9A649C5D9C4A8CC6016CC9B4229F3399629A0C3005E797A5040C016A00DD40010B8E508615000213112294749B8D67EC45F63A980233D8BCF1DC44FAC017914993D42C9000282CB9D4A776233B4BF361F2F9F6659CE5764EB9A3E9007ED3B7B6896C0159F9D1EE76B3FFEF4B8FCF3B88019316E51DA181802B400A8CFCC127E60935D7B10078C01F8B50B20E1803D1FA21C6F300661AC678946008C918E002A72A0F27D82DB802B239A63BAEEA9C6395D98A001A9234EA620026D1AE5CA60A900A4B335A4F815C01A800021B1AE2E4441006A0A47686AE01449CB5534929FF567B9587C6A214C6212ACBF53F9A8E7D3CFF0B136FD061401091719BC5330E5474000D887B24162013CC7EDDCDD8E5E77E53AF128B1276D0F980292DA0CD004A7798EEEC672A7A6008C953F8BD7F781ED00395317AF0726E3402100625F3D9CB18B546E2FC9C65D1C20020E4C36460392F7683004A77DB3DB00527B5A85E06F253442014A00010A8F9106108002190B61E4750004262BC7587E801674EB0CCF1025716A054AD47080467A00B864AD2D4B193E92B4B52C64F27BFB05200C165A38DDF8D5A009C9C2463030802879EB55AB8010396069C413005FC01098EDD0A63B742852402B74DF7FDFE8368037700043E2FC2C8CA00087C518990C0C015C00542726C13936392A4633D8F1802532E5801E84FDF34FCA1487D367EF9A7E50A43E90", 2536453523344)
    ],    
)
def test_evaluate(hex_string, expected): # Part 2
    # Given: an input hex string (converted to binary)
    binary_string = solution.hex_string_to_binary_string(hex_string)

    # When: the first outermost packet is gathered from this input 
    packet_list = solution.parse_binary_string_to_packet_list(binary_string)
    outermost_packet = packet_list[0]

    # Then: the evaluated value of this outermost packet is as expected
    assert evaluate_value_from_packet(outermost_packet) == expected