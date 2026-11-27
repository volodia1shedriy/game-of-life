import time
import os

def create_grid(n, m):
    """Create a new grid with n rows and m columns, all cells dead."""
    return [[0] * m for _ in range(n)]

def from_strings(lines):
    """Create a grid from a list of strings. '#' is alive, '.' is dead."""
    return [[1 if char == '#' else 0 for char in line] for line in lines]

def render(grid):
    """Return a string representation of the grid. Alive cells are '#', dead are '.'."""
    return "\n".join(
        "".join("#" if cell == 1 else "." for cell in row)
        for row in grid
    )

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
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

def clear():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def place(grid, pattern, top, left):
    """Place a pattern into the grid at the given position."""
    n = len(grid)
    m = len(grid[0])
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if 0 <= top + i < n and 0 <= left + j < m:
                grid[top + i][left + j] = pattern[i][j]

def run(grid, generations, delay=0.1):
    """Run the game of life animation."""
    for gen in range(generations):
        clear()
        print(f"Поколение {gen}")
        print(render(grid))
        grid = step(grid)
        time.sleep(delay)

if __name__ == "__main__":
    big_grid = create_grid(20, 40)
    
    glider = from_strings([
        ".#.",
        "..#",
        "###"
    ])
    
    place(big_grid, glider, 1, 1)
    
    run(big_grid, 60, 0.1)