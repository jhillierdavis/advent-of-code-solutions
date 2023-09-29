from collections import defaultdict

import strutils

def map_display_digits_with_unique_segments(signals:[str]) -> defaultdict:
    map = defaultdict(int)
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
    return map

def map_next_identifiable_display_digits(map:defaultdict, signals:[str]) -> map:   
    for signal in signals:
        value = strutils.sort_alphabetically(signal)
        if value in map.values():
            continue

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
    return map

def map_remaining_display_digits(map:defaultdict, signals:[str]) -> map:   
    # Map remaining non-unique signals
    for signal in signals:
        value = strutils.sort_alphabetically(signal)
        if value in map.values():
            continue
        
        if len(value)== 5:
            if strutils.has_subset_of_chars(map[6], value):
                map[5] = value
            else:
                map[2] = value
    return map

def map_display_digits_to_sorted_signals_segments_from_input(input_signals):
    signals = input_signals.split(" ")

    # Map (digital display to sorted segments) display digits 1,7,4 and 8 (with unique segments)
    map = map_display_digits_with_unique_segments(signals) 
    
    # Map next identifiable display digits from initial set
    map_next_identifiable_display_digits(map, signals)

    # Map next remaining display digits from known set
    map_remaining_display_digits(map, signals) 

    return map