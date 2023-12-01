from helpers import fileutils

def extract_number_from_string(input, digits_only=True):
    num_str = ""
    for i in range(len(input)):
        ch = input[i]
        if ch.isnumeric():
            num_str += ch
        elif digits_only == False:
             substr = input[i:]
             if (substr.startswith('one')):
                  num_str += '1'
             if (substr.startswith('two')):
                  num_str += '2'
             if (substr.startswith('three')):
                  num_str += '3'
             if (substr.startswith('four')):
                  num_str += '4'
             if (substr.startswith('five')):
                  num_str += '5'
             if (substr.startswith('six')):
                  num_str += '6'
             if (substr.startswith('seven')):
                  num_str += '7'
             if (substr.startswith('eight')):
                  num_str += '8'
             if (substr.startswith('nine')):
                  num_str += '9'

    length = len(num_str)

    if length == 1:
           num_str += num_str

    if length > 2:
           num_str = num_str[0] + num_str[length-1]

    #print(f"DEBUG: {num_str}")
    return int(num_str)


def extract_first_and_last_numbers_from_file(filename, digits_only=True):
    lines = fileutils.get_file_lines(filename)

    ans = 0
    for l in lines:
         ans += extract_number_from_string(l, digits_only)
    return ans