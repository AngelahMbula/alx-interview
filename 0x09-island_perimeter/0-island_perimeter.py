#!/usr/bin/python3
def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 to the perimeter
                
                # Check neighboring cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 if the neighbor is also land horizontally
                    
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 if the neighbor is also land vertically
    
    return perimeter
