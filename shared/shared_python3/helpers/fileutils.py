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

def get_file_first_line_to_int_array(filename):
    lines = get_file_lines(filename)

    return [int(numeric_string) for numeric_string in lines[0].split(',')]


def get_lines_before_empty_from_file(filename):
    lines:[] = get_file_lines(filename)

    results = []

    for l in lines:
        if len(l.strip()) == 0 :
            break
        results.append(l)
    return results

def get_lines_after_empty_from_file(filename):
    lines:[] = get_file_lines(filename)

    results = []

    is_past_empty = False
    for l in lines:
        if len(l.strip()) == 0 :
            is_past_empty = True
        elif is_past_empty:    
            results.append(l)
    return results
