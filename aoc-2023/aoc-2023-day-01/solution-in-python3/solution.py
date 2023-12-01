from helpers import fileutils

def get_word_to_digit_map():
     word_to_digit_map = dict()

     word_to_digit_map['one'] = '1'
     word_to_digit_map['two'] = '2'
     word_to_digit_map['three'] = '3'
     word_to_digit_map['four'] = '4'
     word_to_digit_map['five'] = '5'
     word_to_digit_map['six'] = '6'
     word_to_digit_map['seven'] = '7'
     word_to_digit_map['eight'] = '8'
     word_to_digit_map['nine'] = '9'

     return word_to_digit_map

def extract_all_numbers_from_string(input, word_to_digit_map, digits_only=True):
    num_str = ""
    for i in range(len(input)):
        ch = input[i]
        if ch.isnumeric():
            num_str += ch
        elif digits_only == False:
             substr = input[i:]

             for k in word_to_digit_map.keys():
                if (substr.startswith(k)):
                  num_str += word_to_digit_map[k]
                  break
    return num_str     


def extract_calibration_value_from_string(input, digits_only=True):
    word_to_digit_map = get_word_to_digit_map()

    num_str = extract_all_numbers_from_string(input, word_to_digit_map, digits_only)

    length = len(num_str)

    if length == 1: # First == last, so duplicate
           num_str += num_str
    elif length > 2: # Get first + last
           num_str = num_str[0] + num_str[length-1]

    #print(f"DEBUG: {num_str}")
    return int(num_str) # Convert to integer value


def extract_calibration_value_sum_from_file(filename, digits_only=True):
    lines = fileutils.get_file_lines(filename)

    ans = 0
    for l in lines:
         ans += extract_calibration_value_from_string(l.lower(), digits_only)
    return ans