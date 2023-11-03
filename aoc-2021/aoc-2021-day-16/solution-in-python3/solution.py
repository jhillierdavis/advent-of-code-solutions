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


#def binary_to_hex(binary_str):
#    return '%08X' % int(binary_str, 2)    

def get_packet_version_sum_recursively(packet) -> int:
    print(f"DEBUG: [get_packet_version_sum_recursively] packet={packet}")
    version_sum = packet.get_version()
    if packet.is_operator():
        for p in packet.get_sub_packets():        
            version_sum += get_packet_version_sum_recursively(p)
    return version_sum

def get_version_sum(hex_string:str) -> int:
    packet = parse_to_packet(hex_string)    
    return get_packet_version_sum_recursively(packet)


class Packet():

    def __init__(self, binary_string):
        print(f"DEBUG: Constructing packet from binary_string: {binary_string}")
        self.binary_string = binary_string

        version = int(binary_string[0:3], 2)
        type_id = int(binary_string[3:6], 2)

        self.version = version
        self.type_id = type_id

    def get_version(self):
        return self.version
    
    def get_type_id(self):
        return self.type_id
    
    def is_literal(self) -> bool:
        return self.get_type_id() == 4
    
    def is_operator(self) -> bool:
        return not self.is_literal()
    
    def get_sub_packets(self) -> []:
        if self.is_literal():
            return None
        
        if self.binary_string == "" or int(self.binary_string) == 0:
            return []
        
        length_type_id = int(self.binary_string[6:7]) 
        if length_type_id == 0:
            sub_packets = self.get_length_type_zero_sub_packets()
        else:   
            sub_packets = self.get_length_type_one_sub_packets()
        return sub_packets


    def get_length_type_zero_sub_packets(self):   
        print(f"DEBUG: [get_length_type_zero_sub_packets] for packet={self}")
        
        
        str_length = self.binary_string[7:22] # 15 bits
        #assert len(str_length) == 15, f"str_length={str_length}"   
        if len(str_length) < 15:
            return []     
        
        length = int(str_length,2)
        #print(f"DEBUG: [get_length_type_zero_sub_packets] length={length}")

        packets = []
        number_of_packets = length//11  # TODO: Cannot assume literals!
        for i in range(number_of_packets):
            offset = 22 + (i*11)
            binary_str = self.binary_string[offset:22 + length] if i == (number_of_packets - 1) else self.binary_string[offset:offset+11]

            #hex_str = binary_to_hex(binary_str)
            if binary_str:
                #print(f"DEBUG: binary_str={binary_str}")
                packet = Packet(binary_str)
                packets.append(packet)        
        return packets
    
    def get_length_type_one_sub_packets(self):
        print(f"DEBUG: [get_length_type_one_sub_packets] for packet={self}")
        
        str_length = self.binary_string[7:18] # 11 bits
        assert len(str_length) == 11, f"str_length={str_length}"
        if len(str_length) < 11:
            return []

        packets = []
        number_of_sub_packets = int(str_length,2) 
        #print(f"DEBUG: [get_length_type_one_sub_packets] number_of_sub_packets: {number_of_sub_packets}")
        for i in range(number_of_sub_packets):
            offset = 18 + (i * 11)
            binary_str = self.binary_string[offset:] if i >= (number_of_sub_packets - 1) else  self.binary_string[offset:offset+11]
            if binary_str:
                print(f"DEBUG:  get_length_type_one_sub_packets i={i} number_of_sub_packet={number_of_sub_packets} binary_str={binary_str}")
                packet = Packet(binary_str)
                packets.append(packet)
        return packets


    def get_literal_value_as_binary_string(self):
        if not self.is_literal():
            raise Exception("Not a literal packet!")

        value = ""
        i = 6
        end = False         
        while not end:
            if self.binary_string[i] == "0": # indicates last value packet
                end = True
            value += self.binary_string[i+1:i+5]
            i += 5
        return value

    def get_literal_value(self):
        return int(self.get_literal_value_as_binary_string(), 2)
    
    def get_length_type_id(self):
        if not self.is_operator():
            raise Exception("Not an operator packet!")        
        return int(self.binary_string[6:7])
    
    def get_sub_packet_literals(self):
        sub_packets = []
        
        if self.get_length_type_id() == 0:
            packets = self.get_length_type_zero_sub_packets()
            for p in packets:
                sub_packets.append(p.get_literal_value())
        else:   
            packets = self.get_length_type_one_sub_packets()
            for p in packets:
                sub_packets.append(p.get_literal_value())
        return sub_packets

    def __str__(self):
        readable = "Packet: id: " + str(id(self)) \
            + ", binary_string: " + self.binary_string \
            + ", version: " + str(self.get_version()) \
            + ", type_id: " + str(self.get_type_id())     
        return readable




def parse_to_packet(hex_string):
    map = create_hex_to_binary_map()
    binary_string = hex_to_binary(map, hex_string)
    
    print(f"DEBUG: hex_string: {hex_string} binary_string: {binary_string}")
    return Packet(binary_string)