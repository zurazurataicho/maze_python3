import random

WIDTH = 59
HEIGHT = 21

class Vector:
    start_vec = 0
    vec = 0
    def __init__(self):
        self.reset_vec()
    def reset_vec(self):
        self.vec = random.randint(0, 3)
        self.start_vec = self.vec
    def get_vec(self):
        if self.vec == 0:
            return [0, -1]
        elif self.vec == 1:
            return [0, 1]
        elif self.vec == 2:
            return [-1, 0]
        elif self.vec == 3:
            return [1, 0]
    def rotate_vec(self):
        self.vec += 1
        if self.vec == 4:
            self.vec = 0
        if self.vec == self.start_vec:
            return True
        return False

class Maze:
    ROAD = 0
    WALL = 1
    width = 5
    height = 5
    maze_map = []
    def __init__(self, w, h):
        self._set_size(w, h)
        self._alloc_map()
    def _set_size(self, w, h):
        self.width = w
        self.height = h
    def _alloc_map(self):
        for x in range(self.width):
            self.maze_map.append([Maze.ROAD] * self.height)
    def clear(self):
        for y in range(self.height):
            for x in range(self.width):
                self.maze_map[x][y] = Maze.WALL
    def make_maze(self, x, y):
        v = Vector()
        while True:
            vx, vy = v.get_vec()
            px = x + vx * 2
            py = y + vy * 2
            if px < 0 or px >= self.width or py < 0 or py >= self.height or self.maze_map[px][py] != Maze.WALL:
                if v.rotate_vec():
                    return
                continue
            self.maze_map[x + vx][y + vy] = Maze.ROAD
            self.maze_map[px][py] = Maze.ROAD
            self.make_maze(px, py)
            v.reset_vec()
    def rand_odd(self, mod):
        r = random.randint(1, mod)
        if r % 2 == 0:
            r += 1
        if r > mod:
            r -= 2
        return r
    def make(self):
        x = self.rand_odd(self.width - 2)
        y = self.rand_odd(self.height - 2)
        print("({0}, {1})".format(x, y))
        self.make_maze(x, y)
    def print_maze(self):
        c = ''
        for y in range(self.height):
            for x in range(self.width):
                print('#' if self.maze_map[x][y] == Maze.WALL else ' ', end="")
            print("")

m = Maze(WIDTH, HEIGHT)
for i in range(3):
    m.clear()
    m.make()
    m.print_maze()
