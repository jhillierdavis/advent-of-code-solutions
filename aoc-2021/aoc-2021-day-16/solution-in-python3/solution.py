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


def hex_string_to_binary_string(hex_string):
    map = create_hex_to_binary_map()
    binary_string = hex_to_binary(map, hex_string)
    return binary_string


def get_version_sum_for_packet(packet) -> int:
    version_sum = packet.get_header().get_version()
    #print(f"DEBUG: version_sum={version_sum} for {packet}")
    if packet.get_header().is_operator():
        for sp in packet.get_sub_packets():
            version_sum += get_version_sum_for_packet(sp)
    return version_sum


def parse_hex_string_to_packet_version_sum(hex_string):
    map = create_hex_to_binary_map()
    binary_string = hex_to_binary(map, hex_string)

    packet_list = parse_binary_string_to_packet_list(binary_string)

    sum = 0
    for p in packet_list:
        sum += get_version_sum_for_packet(p)
    return sum


def get_next_packet_literal(packet_header, binary_string):
        value = ""
        i = 6 # Header offset
        end = False         
        while not end: 
            if binary_string[i] == "0": # indicates last value packet
                end = True
            value += binary_string[i+1:i+5]
            i += 5
        packet = PacketLiteral(packet_header, value, i)
        return packet


def parse_binary_string_to_next_packet(binary_string:str) :
    if len(binary_string) < 11:
        return None

    # Determine the packet header
    packet_header = PacketHeader(binary_string)

    if packet_header.is_literal():
        packet = get_next_packet_literal(packet_header, binary_string)
        #print(f"Processing Literal Packet: {packet}")
        return packet
    
    # Operator
    packet = PacketOperator(packet_header, int(binary_string[6]))

    if packet.get_operator_type_id() == 0:        
        value = binary_string[7:22]
        num_bits = int(value, base=2)
        packet.set_body(binary_string[7:22+num_bits])
        sub_packets = parse_binary_string_to_packet_list(binary_string[22:22+num_bits])
        for sp in sub_packets:
            packet.add_sub_packet(sp)    
        #print(f"Processing Operator Packet (type 0): {packet}")    
        return packet
    
    if packet.get_operator_type_id() == 1:
        offset = 18
        num_packs = int(binary_string[7:offset], base=2)
        while num_packs > 0:
            sub_packet = parse_binary_string_to_next_packet(binary_string[offset:])
            #print(f"DEBUG: Adding sub-packet: {sub_packet}")
            offset += sub_packet.get_bit_length()                        
            packet.add_sub_packet(sub_packet)            
            #print(f"DEBUG: Processing Operator Packet (type 1): {packet} offset={offset} num_packs={num_packs}")
            num_packs -= 1
        #print(f"Processing Operator Packet (type 1): {packet}")    
        return packet

    return None


def parse_binary_string_to_packet_list(binary_string:str) -> []:
    packet_list = []
    offset = 0

    while True:
        remainder = binary_string[offset:]
        #print(f"DEBUG: parse_binary_string_to_packet_list: remainder={remainder}")

        if len(remainder) < 11:
            break

        next_packet = parse_binary_string_to_next_packet(remainder)
        if not next_packet:
            break

        offset += next_packet.get_bit_length()
        packet_list.append(next_packet)
        
    return packet_list


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


class PacketHeader():

    def __init__(self, binary_string):
        #print(f"DEBUG: Constructing packet header from binary_string: {binary_string}")

        self.bits = binary_string[0:6]

        version = int(binary_string[0:3], 2)
        type_id = int(binary_string[3:6], 2)

        self.version = version
        self.type_id = type_id

    def get_bits(self):
        return self.bits
    
    def get_bit_length(self):
        return len(self.bits)

    def get_version(self):
        return self.version
    
    def get_type_id(self):
        return self.type_id
    
    def is_literal(self) -> bool:
        return self.get_type_id() == 4
    
    def is_operator(self) -> bool:
        return not self.is_literal()
    
    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        readable = "PacketHeader: id: " + str(id(self)) \
            + ", bits: " + self.get_bits() \
            + ", bit_length: " + str(self.get_bit_length()) \
            + ", version: " + str(self.get_version()) \
            + ", type_id: " + str(self.get_type_id())  
           
        return readable


class PacketLiteral:

    def __init__(self, packet_header:PacketHeader, body:str, bit_length:int):
        self.packet_header = packet_header
        self.body = body
        self.bit_length = bit_length

    def get_header(self):
        return self.packet_header
    
    def get_body(self):
        return self.body

    def get_value(self):
        return int(self.body,2)

    def get_bit_length(self):
        return self.bit_length

    def __str__(self):
        readable = "PacketLiteral: id: " + str(id(self)) \
            + ", header: " + str(self.get_header()) \
            + ", body: " + str(self.get_body()) \
            + ", value: " + str(self.get_value()) \
            + ", bit_length: " + str(self.get_bit_length())
        return readable   


class PacketOperator:

    def __init__(self, packet_header:PacketHeader, operator_type_id:int):
        self.packet_header = packet_header
        self.operator_type_id = operator_type_id
        self.sub_packets = [] # Retain order via a list
        self.body = ""

    def get_header(self):
        return self.packet_header
    
    def get_operator_type_id(self) -> int:
        return self.operator_type_id
    
    def get_number_of_sub_packets(self) -> int:
        return len(self.sub_packets)
    
    def add_sub_packet(self, sub_packet):
        if sub_packet:
            self.sub_packets.append(sub_packet)

    def get_sub_packets(self):
        return self.sub_packets
    
    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body

    def get_bit_length(self):
        prefix_length = 18
        if self.get_operator_type_id() == 0:
            prefix_length = 22
        for sp in self.get_sub_packets():
            prefix_length += sp.get_bit_length()
        return prefix_length 


    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        readable = "PacketOperator: id: " + str(id(self)) \
            + ", header: " + str(self.get_header()) \
            + ", operator_type_id: " + str(self.get_operator_type_id()) \
            + ", number_of_sub_packets: " + str(self.get_number_of_sub_packets()) \
            + ", body: " + str(self.get_body()) \
            + ", bit_length: " + str(self.get_bit_length())
        return readable           