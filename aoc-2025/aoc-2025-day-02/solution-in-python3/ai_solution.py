"""
AI Prompt:

Write a python function to check whether an input number contains is the equal of the combination of half the provided number 

e.g.: the following should return True: 
* 55 (since 5 twice) 
* 6464 (since 64 twice)
* 123123 (since 123 twice

"""


def is_double_half(num: int) -> bool:
    """
    Check if the given number consists of two identical halves.
    Examples:
        55 -> True  (5 repeated twice)
        6464 -> True (64 repeated twice)
        123123 -> True (123 repeated twice)
        1234 -> False
    """
    s = str(num)
    length = len(s)

    # Must have even length to split into two halves
    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]

"""
AI Prompt:

Create a more general function that matches any fully repeating sequence of numbers 
e.g. 2121212121 (which has 21 repeating throughout)
"""

def is_repeating_sequence(num: int) -> bool:
    """
    Check if the given number consists of a repeating sequence.
    Examples:
        55 -> True   ("5" repeated)
        6464 -> True ("64" repeated)
        123123 -> True ("123" repeated)
        2121212121 -> True ("21" repeated)
        1234 -> False
    """
    s = str(num)
    length = len(s)

    # Try all possible substring lengths up to half the total length
    for i in range(1, length // 2 + 1):
        if length % i == 0:  # substring must evenly divide the string
            piece = s[:i]
            if piece * (length // i) == s:
                return True
    return False


"""
AI Prompt:

Write Python code that does the following:

Defines a function `sum_double_half_in_ranges(filename: str) -> dict`:
   - Read the first line of the file.
   - The line contains a comma-separated list of ranges in the form `min-max`.
   - For each range:
     - Iterate through all numbers from min to max inclusive.
     - Use `is_double_half` to check each number.
     - If True, add the number to a running sum for that range.
   - Return a dictionary mapping each range string (e.g. "55-65") to the sum of matching numbers.

Make the code robust, with error handling for invalid range formats, and efficient enough to handle large ranges.
"""

def sum_double_half_in_ranges(filename: str) -> dict:
    """
    Read a comma-separated list of ranges from the first line of a file
    and count repeating-sequence numbers in each range.

    File format: first line contains 'min-max' ranges separated by commas.
    Example line: 1188511880-1188511890,55-65,6464-6470
    Returns: dict mapping 'min-max' string to count of matches.
    """
    results = {}
    with open(filename, "r") as f:
        first_line = f.readline().strip()
        if not first_line:
            return results

        ranges = [rng.strip() for rng in first_line.split(",") if rng.strip()]

        for rng in ranges:
            try:
                min_val_str, max_val_str = rng.split("-")
                min_val, max_val = int(min_val_str), int(max_val_str)
            except ValueError:
                raise ValueError(f"Invalid range format: {rng}")

            count = 0
            for num in range(min_val, max_val + 1):
                if is_double_half(num):
                    count += num

            results[rng] = count
    return results


def solve_part1(filename):
    ans = 0
    counts = sum_double_half_in_ranges(filename)
    for rng, total in counts.items():
        ans += total
    return ans


"""
AI Prompt:

Write Python code that does the following:

1. Define a function `is_repeating_sequence(num: int) -> bool`:
   - Convert the number to a string.
   - Return True if the string can be constructed by repeating a smaller substring (e.g. 55 → "5" repeated, 6464 → "64" repeated, 123123 → "123" repeated, 2121212121 → "21" repeated).
   - Otherwise return False.

2. Define a function `sum_repeating_in_ranges(filename: str) -> dict`:
   - Read the first line of the file.
   - The line contains a comma-separated list of ranges in the form `min-max`.
   - For each range:
     - Iterate through all numbers from min to max inclusive.
     - Use `is_repeating_sequence` to check each number.
     - If True, add the number to a running sum for that range.
   - Return a dictionary mapping each range string (e.g. "55-65") to the sum of matching numbers.

Make the code robust, with error handling for invalid range formats, and efficient enough to handle large ranges.
"""

def sum_repeating_in_ranges(filename: str) -> dict:
    """
    Read a comma-separated list of ranges from the first line of a file
    and sum the values of repeating-sequence numbers in each range.

    File format: first line contains 'min-max' ranges separated by commas.
    Example line: 1188511880-1188511890,55-65,6464-6470
    Returns: dict mapping 'min-max' string to sum of matching values.
    """
    results = {}
    with open(filename, "r") as f:
        first_line = f.readline().strip()
        if not first_line:
            return results

        ranges = [rng.strip() for rng in first_line.split(",") if rng.strip()]

        for rng in ranges:
            try:
                min_val_str, max_val_str = rng.split("-")
                min_val, max_val = int(min_val_str), int(max_val_str)
            except ValueError:
                raise ValueError(f"Invalid range format: {rng}")

            total_sum = 0
            for num in range(min_val, max_val + 1):
                if is_repeating_sequence(num):
                    total_sum += num

            results[rng] = total_sum
    return results


def solve_part2(filename):
    ans = 0
    counts = sum_repeating_in_ranges(filename)
    for rng, total in counts.items():
        ans += total
    return ans