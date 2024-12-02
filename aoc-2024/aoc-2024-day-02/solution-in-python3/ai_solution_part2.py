# Solve using AI (e.g. Co-Pilot)
# ------------------------------
#
# Ref. https://copilot.microsoft.com/chats
#
# Prompt:
#
# "Create a python program to process each line of a file counting the number of lines as a set of integers, where a sub-set of each line of integers expect one is either always increasing or decreasing by at least 1 and up to 3."
#

def is_valid_subsequence_with_one_exception(numbers):
    for i in range(len(numbers)):
        subset = numbers[:i] + numbers[i+1:]
        increasing = all(1 <= subset[j] - subset[j-1] <= 3 for j in range(1, len(subset)))
        decreasing = all(-3 <= subset[j] - subset[j-1] <= -1 for j in range(1, len(subset)))
        if increasing or decreasing:
            return True
    return False

def count_valid_lines_with_one_exception(file_path):
    valid_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            if is_valid_subsequence_with_one_exception(numbers):
                valid_count += 1
    return valid_count



# Counting the valid lines
valid_lines_count = count_valid_lines_with_one_exception('AOC-2024-Day-02_Puzzle-Input-Example.txt')
print(f"Part 2: Number of valid lines (in example input): {valid_lines_count}")
assert valid_lines_count == 4

# Counting the valid lines
valid_lines_count = count_valid_lines_with_one_exception('AOC-2024-Day-02_Puzzle-Input-Full.txt' )
print(f"Part 2: Number of valid lines (in full input): {valid_lines_count}")
assert valid_lines_count == 561