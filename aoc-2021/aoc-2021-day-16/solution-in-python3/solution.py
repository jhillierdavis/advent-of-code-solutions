
# TODO
#class Segment():



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
    for p in packet.get_sub_packets():
        version_sum += get_packet_version_sum_recursively(p)
    return version_sum

def get_version_sum(hex_string:str) -> int:
    map = create_hex_to_binary_map()
    binary_string = hex_to_binary(map, hex_string)
    print(f"DEBUG: binary_string={binary_string}")
    packet = Packet(binary_string, False)
    
    return get_packet_version_sum_recursively(packet)


class Packet():
    _map = create_hex_to_binary_map()

    def __init__(self, input_string, is_hex:bool=True):        
        self.binary = hex_to_binary(self._map, input_string) if is_hex else input_string

    
    def get_version(self):
        version_str = self.binary[0:3]
        return int(version_str, 2)
    
    def get_type_id(self):
        type_id_str = self.binary[3:6]
        return int(type_id_str, 2)   

    def get_literal_value(self):
        return int(self.binary[7:11] + self.binary[12:16] + self.binary[17:21], 2)
    
    def is_literal(self) -> bool:
        return self.get_type_id() == 4
    
    def is_operator(self) -> bool:
        return not self.is_literal()
    
    def get_length_type_id(self):
        return int(self.binary[6:7])
    
    def get_sub_packets(self):
        sub_packets = []

        if self.get_length_type_id() == 0:
            length = int(self.binary[7:22],2)
            print(f"DEBUG: length_type_id:0 length={length}")
            for i in range(2):
                offset = 22 + (i*11)
                binary_str = self.binary[offset:offset+11] if i == 0 else self.binary[offset:offset+(27-11)]

                #hex_str = binary_to_hex(binary_str)
                print(f"DEBUG: binary_str={binary_str}")
                packet = Packet(binary_str, False)
                sub_packets.append(packet)
        else:   
            length = int(self.binary[7:18],2)
            print(f"DEBUG: length_type_id:1 length={length}")
            for i in range(length):
                offset = 18 + (i * 11)
                binary_str = self.binary[offset:offset+11]
                #hex_str = binary_to_hex(binary_str)
                print(f"DEBUG: binary_str={binary_str}")
                packet = Packet(binary_str, False)
                sub_packets.append(packet)
                
        return sub_packets        
    
    def get_sub_packet_literals(self):
        sub_packets = []
        
        if self.get_length_type_id() == 0:
            length = int(self.binary[7:22],2)
            print(f"DEBUG: length_type_id = 0 length={length}")
            for i in range(2):
                offset = 22 + (i*11)
                binary_str = self.binary[offset:offset+11] if i == 0 else self.binary[offset:offset+(27-11)]

                #hex_str = binary_to_hex(binary_str)
                print(f"DEBUG: binary_str={binary_str}")
                packet = Packet(binary_str, False)
                sub_packets.append(packet.get_literal_value())
        else:   
            length = int(self.binary[7:18],2)
            print(f"DEBUG: length={length}")
            for i in range(length):
                offset = 18 + (i * 11)
                binary_str = self.binary[offset:offset+11]
                #hex_str = binary_to_hex(binary_str)
                print(f"DEBUG: binary_str={binary_str}")
                packet = Packet(binary_str, False)
                sub_packets.append(packet.get_literal_value())
        """           
        sub_packet_literals = []

        for p in self.get_sub_packets():
            literals = p.get_sub_packet_literals()
            for l in literals():
                sub_packet_literals.append(l)
         
        return sub_packet_literals
        """
        return sub_packets
    

    def __str__(self):
        readable = "Packet: id: " + str(id(self)) \
            + ", binary: " + self.binary \
            + ", version: " + str(self.get_version()) \
            + ", type_id: " + str(self.get_type_id()) \
            + ", literal: " + str(self.is_literal())                                               
        return readable
