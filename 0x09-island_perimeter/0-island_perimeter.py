#!/usr/bin/python3
"""
island_perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
        grid (list): A list of lists representing the grid.
                     0 represents water, and 1 represents land.
                     The grid is rectangular with width and
                     height not exceeding 100.

    Returns:
        int: The perimeter of the island.

    Raises:
        ValueError: If the grid is empty or not rectangular.

    Notes:
        - Cells are connected horizontally/vertically but not diagonally.
        - The grid is completely surrounded by water.
        - There is only one island (or nothing).
        - The island doesn't have "lakes" (water inside that isn't
        connected to the water surrounding the island).
    """

    if not grid or not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("Invalid grid: The grid must be"
                         "non-empty and rectangular.")

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check left neighbor
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # Check right neighbor
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

                # Check top neighbor
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # Check bottom neighbor
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter
