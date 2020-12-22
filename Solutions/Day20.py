inpt = open("input.txt").read().strip().split("\n\n")


class Tile:
    def __init__(self, num, tile):
        self.num = num
        self.tile = tile  # [row, row, row, ...]

        self.connected = [None, None, None, None]  # top, bottom, left, right

    def get_sides(self):
        return self.get_top_side(), self.get_bottom_side(), self.get_left_side(), self.get_right_side()

    def get_connections(self):
        return self.connected

    def get_num_connections(self):
        return sum(i is not None for i in self.get_connections())

    def connect_tiles(self, other_tile):
        my_sides = self.get_sides()
        other_sides = other_tile.get_sides()

        for i1, s1 in enumerate(my_sides):
            for i2, s2 in enumerate(other_sides):
                if s1 == s2 or s1[::-1] == s2:
                    self.connected[i1] = other_tile
                    other_tile.connected[i2] = self

                    return True
        return False

    def flip_horizontal(self):
        self.tile = [i[::-1] for i in self.tile]

        self.connected[3], self.connected[2] = self.connected[2], self.connected[3]

    def flip_vertical(self):
        self.tile = self.tile[::-1]

        self.connected[0], self.connected[1] = self.connected[1], self.connected[0]

    def transpose(self):
        temp = ["" for i in range(len(self.tile[0]))]

        for i in self.tile:
            for j, k in enumerate(i):
                temp[j] += k

        self.tile = temp

        self.connected[0], self.connected[2] = self.connected[2], self.connected[0]
        self.connected[1], self.connected[3] = self.connected[3], self.connected[1]

    def rotate_cw(self):
        self.transpose()

        self.flip_horizontal()

    def rotate_ccw(self):
        self.flip_horizontal()

        self.transpose()

    def get_left_side(self):
        return ''.join(map(lambda x: x[0], self.tile))

    def get_right_side(self):
        return ''.join(map(lambda x: x[-1], self.tile))

    def get_top_side(self):
        return self.tile[0]

    def get_bottom_side(self):
        return self.tile[-1]

    def orient_top(self, tile):
        while self.connected[0] is not tile:
            self.rotate_cw()

        if tile.get_bottom_side() != self.get_top_side():
            self.flip_horizontal()

    def orient_left(self, tile):
        while self.connected[2] is not tile:
            self.rotate_cw()

        if tile.get_right_side() != self.get_left_side():
            self.flip_vertical()

    def orient_row(self):
        if self.connected[3] is not None:
            self.connected[3].orient_left(self)
            self.connected[3].orient_row()

    def orient_col(self):
        if self.connected[1] is not None:
            self.connected[1].orient_top(self)
            self.connected[1].orient_col()

    def get_row(self):
        if self.connected[2] is None:
            return [self]
        return [self] + self.connected[2].get_row()

    def get_col(self):
        if self.connected[1] is None:
            return [self]
        return [self] + self.connected[1].get_col()

    def get_real_map(self):
        return [i[1:-1] for i in self.tile][1:-1]


tiles = [Tile(int(a.split('\n')[0][5:9]), a.split("\n")[1:]) for a in inpt]
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        tiles[i].connect_tiles(tiles[j])

total = 1

for i in tiles:
    if i.get_num_connections() == 2:
        total *= i.num

print(total)

top_left = None # hehe bottom left
for i in tiles:

    if i.connected[0] is None and i.connected[2] is None:
        top_left = i

assert isinstance(top_left, Tile)
top_left.orient_col()

starting_col = top_left.get_col()

for col in starting_col:
    col.orient_row()

temp_map = [col.get_row() for col in starting_col]
l = len(temp_map[0][0].get_real_map())

full_map = ["" for i in range(len(temp_map) * l)]
for i, row in enumerate(temp_map):
    for tile in row:
        for index, mini_row in enumerate(tile.get_real_map()):
            full_map[i*l+index] += mini_row

def check_monster(coord, board): # row col
    good = True
    row, col = coord

    monster = [
        '..................#.',
        '#....##....##....###',
        '.#..#..#..#..#..#...'
    ]

    for r_shift, r in enumerate(monster):
        for c_shift, char in enumerate(r):
            if char == "." or board[row+r_shift][col+c_shift] == "#":
                continue
            else:
                good = False
        if not good:
            break

    return good

temp = Tile(0, full_map) # I already added rotations and shit to this lol
coordinates = set()

for rotate in range(4):
    temp.rotate_cw()

    for flip_h in range(2):
        temp.flip_horizontal()

        for i in range(len(full_map) - 3):
            for j in range(len(full_map[0]) - 20):
                if check_monster((i, j), temp.tile):
                    coordinates.add((i, j))

    for flip_v in range(2):
        temp.flip_vertical()

        for i in range(len(full_map) - 3):
            for j in range(len(full_map[0]) - 20):
                if check_monster((i, j), temp.tile):
                    coordinates.add((i, j))

total = sum(i.count("#") for i in temp.tile)
print(total - 15 * len(coordinates))
