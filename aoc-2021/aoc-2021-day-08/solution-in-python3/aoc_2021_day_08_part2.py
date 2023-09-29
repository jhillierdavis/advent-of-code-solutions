from collections import defaultdict

# Local imports
import strutils
import fileutils
import decypher_digital_display as decypher

def decipher_output_values(input:str) -> int:
    parts = input.split("|")
    input_signals = parts[0]
    input_displays = parts[1]

    map_display_digit_to_sorted_segments = decypher.map_display_digits_to_sorted_signals_segments_from_input(input_signals)

    displays = input_displays.split(" ")
    result = ""
    for display in displays:
        for (key, value) in map_display_digit_to_sorted_segments.items():
            if value == strutils.sort_alphabetically(display):
                result += str(key) # Concatonate matched digitial display values

    return int(result) # Convert to int (e.g. for subsequent ease of addition)

def decipher_total_from_file(filename):
    lines = fileutils.get_file_lines(filename)

    count = 0
    for line in lines:
        count += decipher_output_values(line)

    return count