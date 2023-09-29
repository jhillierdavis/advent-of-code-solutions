import decypher_digital_display as decypher

import strutils

def test_map_display_digits_to_sorted_signals_segments_from_input():
    # Given: input notes
    input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"

    # When: decyphered
    map = decypher.map_display_digits_to_sorted_signals_segments_from_input(input)

    # Then: display digits are correctly mapped to segments
    assert map[5] == strutils.sort_alphabetically("cdfeb")
    assert map[3] == strutils.sort_alphabetically("fcadb")