#!/usr/bin/python3
def island_perimeter(grid):
    """
    Args:
        grid (_type_): _description_
    """
    perimeter = 0
    rows = len(grid)
    cols= len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:

                if i == 0 or grid[i - 1][j] == 0:
                    perimeter +=1

                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i - 1][i] == 0:
                    perimeter +=1
                if j == rows - 1 or grid[i + 1][i] == 0:
                    perimeter += 1
        return perimeter