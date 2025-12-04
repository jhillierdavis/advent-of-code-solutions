# grid_at_count.py

"""
AI Prompt:
(NB: from prompt: "Please provide the prompt that would have generated this output from the outset".  AI code generated iteratively via refined prompting)

Create Python code to count the total number of points with the symbol @ in a two‑dimensional grid that have fewer than 4 immediate neighbouring points (including diagonals) with the same symbol.

Provide the solution as a reusable function and a wrapper that accepts multiline string input.

Also capture the following example grid in unit tests using Pytest, verifying that the count is 13:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Include additional unit tests for edge cases such as a single @ and a fully surrounded 3×3 block of @.
"""

def count_sparse_at_points(grid: list[str]) -> int:
    """
    Count the number of '@' points in the grid that have
    fewer than 4 immediate neighbours (including diagonals)
    also equal to '@'.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    total = 0

    # 8 directions: orthogonal + diagonals
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                neighbours = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                        neighbours += 1

                if neighbours < 4:
                    total += 1
    return total


def solve_from_text(input_text: str) -> int:
    """
    Convenience wrapper: takes multiline string input and returns the count.
    """
    grid = input_text.strip().splitlines()
    return count_sparse_at_points(grid)



"""
AI Prompt:

Write a python function to return the contents of a text file as a string
"""

def read_file_as_string(file_path):
    """
    Reads the contents of a text file and returns it as a string.
    
    :param file_path: Path to the text file
    :return: String containing the file contents
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except Exception as e:
        return f"An error occurred: {e}"