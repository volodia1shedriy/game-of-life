def create_grid(n, m):
    """Create a new grid with n rows and m columns, all cells dead."""
    grid = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        grid.append(row)
    return grid


def from_strings(lines):
    """Create a grid from a list of strings. '#' is alive, '.' is dead."""
    grid = []
    for line in lines:
        row = []
        for char in line:
            if char == '#':
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid


def render(grid):
    """Return a string representation of the grid. Alive cells are '#', dead are '.'."""
    result = ""
    for row in grid:
        line_string = ""
        for cell in row:
            if cell == 1:
                line_string = line_string + "#"
            else:
                line_string = line_string + "."
        result = result + line_string + "\n"
    
    # Remove the last newline character so there is no empty line at the end
    return result[:-1]

def count_neighbors(grid, i, j):
    """Count living neighbors of cell (i, j). Cells outside the grid are dead."""
    n = len(grid)
    m = len(grid[0])
    count = 0
    
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if grid[ni][nj] == 1:
                    count += 1
    return count


def step(grid):
    """Return the next generation. Does not modify the original grid."""
    n = len(grid)
    m = len(grid[0])
    new_grid = create_grid(n, m)
    
    for i in range(n):
        for j in range(m):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid