import fileutils

def count_words_by_length(input_str:str, list_word_sizes:[int]) -> int:
    words = input_str.split(" ")

    #print(f"DEBUG: words={words}")

    count = 0
    for word in words:
        if len(word) in list_word_sizes:
            count += 1
    return count

def count_words_by_length_from_file(filename:str, list_word_sizes:[int]) -> int:
    lines = fileutils.get_file_lines(filename)

    count = 0
    for line in lines:
        parts = line.split("|")
        count += count_words_by_length(parts[1], list_word_sizes)

    return count


from collections import defaultdict
import strutils

def decipher_signals_to_digits(input_signals):
    map = defaultdict(int)

    signals = input_signals.split(" ")

    # Map unique signals (to corresonding digits)
    for signal in signals:
        count_signal_segments = len(signal)
        value = strutils.sort_alphabetically(signal)
        if count_signal_segments == 2:
            map[1] = value
        elif count_signal_segments == 3:
            map[7] = value
        elif count_signal_segments == 4:
            map[4] = value
        elif count_signal_segments == 7:
            map[8] = value

    # Map identifiable non-unique signals
    for signal in signals:
        value = strutils.sort_alphabetically(signal)
        if value in map.values():
            continue

        #print(f"DEBUG: {count_signal_segments} {value}")
        count_signal_segments = len(value)
        if count_signal_segments == 5:
            if strutils.has_subset_of_chars(value, map[7]):
                map[3] = value
        elif count_signal_segments == 6:
            if strutils.has_subset_of_chars(value, map[7]):
                if strutils.has_subset_of_chars(value, map[4]):
                    map[9] = value        
                else:
                    map[0] = value
            else:
                map[6] = value

    # Map remaining non-unique signals
    for signal in signals:
        value = strutils.sort_alphabetically(signal)
        if value in map.values():
            continue

        #print(f"DEBUG: {count_signal_segments} {value}")
        if len(value)== 5:
            if strutils.has_subset_of_chars(map[6], value):
                map[5] = value
            else:
                map[2] = value

    return map

def display_defaultdict(map:defaultdict):
    for key, value in map.items():
        print(f"DEBUG: key={key} value={value}")

def decipher_output_values(input:str) -> int:
    # 8 has all seven segments (unique)
    # 1 has two segments (unique)
    # 7 has three segments (unique)
    # 4 has four segments (unique)
    # Top segment determined from diff of 7's segemnts & 1's segments    
    # 0 has six segments and contains all 7's three segments
    # 5 has six segments, but not the same segments as zero
    # 9 has five segments and contains all 4's four segments
    # 3 has five segments and contains all 7's three segments (differs from 9's segments)
    # 2 has five segments and contains the top segment
    # 6 has the remaining 5 segments

    parts = input.split("|")

    input_signals = parts[0]
    input_displays = parts[1]
    #print(f"DEBUG: input_signals={input_signals}")
    #print(f"DEBUG: input_displays={input_displays}")

    map_signal_to_digits = decipher_signals_to_digits(input_signals)
    #display_defaultdict(map_signal_to_digits)

    displays = input_displays.split(" ")
    result = ""
    for display in displays:
        for key, value in map_signal_to_digits.items():
            if value == strutils.sort_alphabetically(display):
                #print(f"DEBUG: {key}")
                result += str(key)

    return int(result)

def decipher_total_from_file(filename):
    lines = fileutils.get_file_lines(filename)

    count = 0
    for line in lines:
        count += decipher_output_values(line)

    return count