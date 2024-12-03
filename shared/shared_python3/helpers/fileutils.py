def get_file_lines(filename):
    # Open file by filename supplied
    data_file = open(filename, 'r')

    # Retrieve lines & return via an array (of strings)
    array_lines = []
    for line in data_file:
        content = line.strip('\n').strip() # Remove leading/trailing spaces & newlines
        array_lines.append(content)

    # Close file handle
    data_file.close()    
    return array_lines


def get_file_lines_from(filename):
    return get_file_lines(filename)


def get_lines_to_int_array_from(filename):
    lines = get_file_lines_from(filename)    
    values = [int(numeric_string) for numeric_string in lines]
    return values


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

# TODO: Add unit test coverage (e.g. from AOC 2023 Day 13)
def get_contiguous_non_empty_lines_from(filename):
    lines = get_file_lines(filename)
    num_lines = len(lines)

    response = []
    buffer = []
    for i in range(num_lines):
        l = lines[i]
        is_empty_line = 0 == len(l.strip())
        is_last_line = i == (num_lines - 1)
        is_buffer_populated = len(buffer) > 0

        if not is_empty_line:
            buffer.append(l)            

        if is_empty_line or is_last_line:
            if is_buffer_populated:
                response.append(buffer)
                buffer = []
    return response


def get_text_from(filename):
    text = open(filename).read().strip()
    return text