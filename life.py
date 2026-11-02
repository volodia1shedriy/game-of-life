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