import aoc_2021_day_08_part2 as solution

# Puzzle data
example_file = 'puzzle-input-sample.txt'
full_file = 'puzzle-input-full.txt'

def test_part2_single_line_example():
    input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    assert solution.decipher_output_values(input) == 5353

def test_part2_solution():    
    # When: Solved with example puzzle data
    assert solution.decipher_total_from_file(example_file) == 61229 

    # Then: Solve with full (personalised) data
    assert solution.decipher_total_from_file(full_file) == 1020159    