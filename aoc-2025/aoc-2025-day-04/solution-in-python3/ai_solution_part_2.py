"""
AI Prompt:

Create Python code that processes a two‑dimensional grid of characters.

The task is to:

Identify all points with the symbol @ that have fewer than 4 immediate neighbouring points (including diagonals) also equal to @.

Replace all such points with the symbol x.

Repeat this process iteratively until no more matching points remain.

Return the total number of points replaced (i.e., the number of original @ symbols that eventually became x).

Provide the solution as reusable functions, including a wrapper that accepts multiline string input.

Also capture the following example grid in unit tests using Pytest, verifying that the total replacements equal 43:

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


# grid_replace.py

def find_matching_points(grid: list[list[str]]) -> list[tuple[int, int]]:
    """
    Find all '@' points that have fewer than 4 immediate neighbours (including diagonals)
    also equal to '@'.
    Returns a list of coordinates (row, col).
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    matches = []

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
                    matches.append((r, c))
    return matches


def iterative_replace(input_text: str) -> int:
    """
    Iteratively replace all matching '@' points with 'x' until none remain.
    Return the total number of replacements performed.
    """
    grid = [list(line) for line in input_text.strip().splitlines()]
    total_replaced = 0

    while True:
        matches = find_matching_points(grid)
        if not matches:
            break
        for r, c in matches:
            grid[r][c] = "x"
            total_replaced += 1

    return total_replaced
