import life

def check_create_grid():
    g = life.create_grid(3, 4)
    assert g == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    g[0][0] = 1
    assert g[1][0] == 0

def check_from_strings():
    glider = life.from_strings([".#.", "..#", "###"])
    assert glider == [[0, 1, 0], [0, 0, 1], [1, 1, 1]]

def check_render():
    glider = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    assert life.render(glider) == ".#.\n..#\n###"
    assert life.render([]) == ""
    assert life.render([[0]]) == "."

def check_count_neighbors():
    blinker = life.from_strings(["...", "###", "..."])
    assert life.count_neighbors(blinker, 1, 1) == 2
    assert life.count_neighbors(blinker, 0, 1) == 3
    assert life.count_neighbors(blinker, 0, 0) == 2

def check_step():
    blinker = life.from_strings(["...", "###", "..."])
    assert life.step(blinker) == life.from_strings([".#.", ".#.", ".#."])
    assert life.step(life.step(blinker)) == blinker
    
    block = life.from_strings(["....", ".##.", ".##.", "...."])
    assert life.step(block) == block
    
    before = [row[:] for row in blinker]
    life.step(blinker)
    assert blinker == before, "step must not modify the original grid"

def check_place():
    grid = life.create_grid(5, 5)
    pattern = life.from_strings(["##", "##"])
    life.place(grid, pattern, 1, 1)
    assert grid[1][1] == 1
    assert grid[1][2] == 1
    assert grid[2][1] == 1
    assert grid[2][2] == 1
    assert grid[0][0] == 0

if __name__ == "__main__":
    check_create_grid()
    check_from_strings()
    check_render()
    check_count_neighbors()
    check_step()
    check_place()
    print("All checks passed!")