# Solve using AI (e.g. Co-Pilot)
# ------------------------------
#
# Ref. https://copilot.microsoft.com/chats
#
# Prompt:
#
# "Create a python program to process each line of a file counting the number of lines where each integer value is either always increasing or decreasing by at least 1 and up to 3"
#

def is_consistently_changing_sequence(numbers):
    increasing = all(1 <= numbers[i] - numbers[i-1] <= 3 for i in range(1, len(numbers)))
    decreasing = all(1 <= numbers[i-1] - numbers[i] <= 3 for i in range(1, len(numbers)))
    return increasing or decreasing

def count_consistently_changing_lines(file_path):
    valid_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            if is_consistently_changing_sequence(numbers):
                valid_count += 1
    return valid_count


# Counting the valid lines in example input
valid_lines_count = count_consistently_changing_lines('AOC-2024-Day-02_Puzzle-Input-Example.txt' )
print(f"Part 1: Number of valid lines (in example input): {valid_lines_count}")
assert valid_lines_count == 2

# Counting the valid lines in full input
valid_lines_count = count_consistently_changing_lines( 'AOC-2024-Day-02_Puzzle-Input-Full.txt' ) 
print(f"Part 1: Number of valid lines (in full input): {valid_lines_count}")
assert valid_lines_count == 516