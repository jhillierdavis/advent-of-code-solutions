from helpers import fileutils


def get_char_count(str_input, char):
    return str_input.count(char)


def process_lines_with_predicate(filename, predicate):
    lines = fileutils.get_file_lines_from(filename)

    valid_count = 0
    for l in lines:
        values = l.split(' ')
        #print(f"DEBUG: {values}")

        min = int(values[0].split("-")[0])
        max = int(values[0].split("-")[1])

        char = values[1][-2]

        str_input = values[2]

        #print(f"DEBUG: values={values} min={min} max={max} char={char} str_input={str_input}")

        if predicate(str_input, char, min, max):
                valid_count += 1

    return valid_count


def solve_part1(filename):
    def predicate(str_input, char, min, max):
        count = get_char_count(str_input, char)
        if count >= min and count <= max:
            return True
        return False

    return process_lines_with_predicate(filename, predicate)


def solve_part2(filename):
    def predicate(str_input, char, min, max):
        if char == str_input[min-1] and char == str_input[max-1]:
             return False
        
        if char == str_input[min-1] or char == str_input[max-1]:
            return True
        
        return False

    return process_lines_with_predicate(filename, predicate)
