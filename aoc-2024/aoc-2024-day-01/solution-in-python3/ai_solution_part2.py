# Solve using AI (e.g. Co-Pilot)
# ------------------------------
#
# Ref. https://copilot.microsoft.com/chats
#
# Prompt:
# 
# "Create a python program to read lines from a file where each line contains 2 integers spearated by 3 space characters. 
# Add the first integer in each line to a line and the second integer to another list. 
# For each entry in the first list find the number of occurances in the second list.
# Sum up the mulitple of each entry in the first list with the number of occurances of this entry value in the second list.
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
    
    total_sum = sum(entry1 * list2.count(entry1) for entry1 in list1)
    
    return total_sum

# File path
file_path = 'AOC-2024-Day-01_Puzzle-Input-Example.txt'

# Process the file and print the total sum
total_sum = process_file(file_path)
print(f"Part 2: Total sum (example input): {total_sum}")
assert total_sum == 31

# File path
file_path = 'AOC-2024-Day-01_Puzzle-Input-Full.txt'

# Process the file and print the total sum
total_sum = process_file(file_path)
print(f"Part 2: Total sum (full input): {total_sum}")
assert total_sum == 19437052 
