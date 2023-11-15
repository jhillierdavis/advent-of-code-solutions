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