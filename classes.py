import numpy as np

class desk:
    def __init__(self, w, h, a):
        self.desk = np.int8(np.zeros((h, w)))
        self.w = w
        self.h = h
        self.a = a
        self.alive = []

    def kletka_klic(self, coord = (0, 0)):
        x = coord[0] // self.a
        y = coord[1] // self.a
        if x < self.w + 1 and y < self.h + 1:
            self.delta_color(x, y, self.desk)
        else:
            print("!!!такой клетки нет!!!")

    def delta_color(self, x, y, desk):
        if desk[y][x] == 1:
            desk[y][x] = 0
            self.alive.remove((x, y))
        else:
            desk[y][x] = 1
            self.alive.append((x, y))

    def update(self):
        desk, w, h = self.desk, self.w, self.h
        new_desk = np.int8(np.zeros((h, w)))
        new_alive = []

        proccessed = set()

        for x, y in self.alive:
            for x1 in range(x - 1, x + 2):
                for y1 in range(y - 1, y + 2):
                    proccessed.add((x1 % w, y1 % h))

        for x, y in proccessed:
            c = -desk[y][x]
            for x1 in range(x - 1, x + 2):
                for y1 in range(y - 1, y + 2):
                    c += desk[y1 % h][x1 % w]
            if ((desk[y][x] == 1 and not (c < 2 or c > 3)) or (desk[y][x] == 0 and c == 3)):
                new_desk[y][x] = 1
                new_alive.append((x, y))

        self.desk = new_desk
        self.alive = new_alive
