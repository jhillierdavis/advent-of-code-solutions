def get_file_lines(filename):
    # Open file by filename supplied
    data_file = open(filename, 'r')

    # Retrieve lines & return via an array (of strings)
    array_lines = []
    for line in data_file:
        array_lines.append(line.strip('\n'))

    # Close file handle
    data_file.close()    
    return array_lines

def decimal_value_of_binary_string(binary_string):
    return int(binary_string, 2)
