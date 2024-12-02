# Solve using AI (e.g. Co-Pilot)
# ------------------------------
#
# Ref. https://copilot.microsoft.com/chats
#
# Prompt:
# 
# "Create a python program to read lines from a file where each line contains 2 integers spearated by 3 space characters. 
# Add the first integer in each line to a line and the second integer to another list. 
# Sort both lists. 
# Compare the absolute differences between each entry in the two lists and sum up these differences."
#


def process_file(file_path):
    list1 = []
    list2 = []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split('   ')  # Split by 3 spaces
            if len(parts) == 2:
                list1.append(int(parts[0]))
                list2.append(int(parts[1]))
    
    list1.sort()
    list2.sort()

    total_difference = sum(abs(a - b) for a, b in zip(list1, list2))
    
    return total_difference


# Process the file and print the total difference
total_difference = process_file('AOC-2024-Day-01_Puzzle-Input-Example.txt')
print(f"Part 1: Total absolute difference (example input): {total_difference}")
assert total_difference == 11

# Process the file and print the total difference
total_difference = process_file('AOC-2024-Day-01_Puzzle-Input-Full.txt')
print(f"Part 1: Total absolute difference (full input): {total_difference}")
assert total_difference == 1882714
