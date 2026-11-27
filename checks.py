import life

def check_create_grid():
    g = life.create_grid(3, 4)
    assert g == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    g[0][0] = 1
    assert g[1][0] == 0
    assert life.create_grid(0, 0) == []

def check_from_strings():
    glider = life.from_strings([".#.", "..#", "###"])
    assert glider == [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    lines = ["..#.", "...#", "####"]
    expected = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]]
    assert life.from_strings(lines) == expected

def check_render():
    glider = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    assert life.render(glider) == ".#.\n..#\n###"
    assert life.render([]) == ""
    assert life.render([[0]]) == "."

if __name__ == "__main__":
    check_create_grid()
    check_from_strings()
    check_render()
