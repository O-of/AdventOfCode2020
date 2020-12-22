from typing import Tuple, Dict
from copy import deepcopy

inpt = open("input.txt").read().split("\n")

class Cube3D:
    def __init__(self, position: Tuple[int, int, int], active: bool): # position = x, y, z
        self.position = position
        self.active = active
    def __str__(self):
        return f"Cube({self.position}, {self.active})"
    def __repr__(self):
        return self.__str__()

class Dimention3D:
    def __init__(self, inpt):
        self.current_cubes: Dict[Tuple[int, int, int]: Cube3D] = {(x, y, 0): Cube3D((x, y, 0), cube == "#") for y, row in enumerate(inpt) for x, cube in enumerate(row)}

        self.x_vals = [0, len(inpt[0])-1] # Gives the range of x/y/z values, both are INCLUSIVE
        self.y_vals = [0, len(inpt)-1]
        self.z_vals = [0, 0]

    def get_neighboring_cubes(self, position: Tuple[int, int, int]) -> set:
        return_cubes = set()
        x, y, z = position

        shifts = (-1, 0, 1)

        for x_change in shifts:
            for y_change in shifts:
                for z_change in shifts:
                    if x_change == y_change == z_change == 0:
                        continue
                    else:
                        try:
                            return_cubes.add(self.current_cubes[(x+x_change, y+y_change, z+z_change)])
                        except KeyError:
                            pass

        return return_cubes

    def expand_board(self):
        self.x_vals[0], self.x_vals[1] = self.x_vals[0] - 1, self.x_vals[1] + 1
        self.y_vals[0], self.y_vals[1] = self.y_vals[0] - 1, self.y_vals[1] + 1
        self.z_vals[0], self.z_vals[1] = self.z_vals[0] - 1, self.z_vals[1] + 1

        for x in self.x_vals:
            for y in range(self.y_vals[0], self.y_vals[1] + 1):
                for z in range(self.z_vals[0], self.z_vals[1] + 1):
                    self.current_cubes[(x, y, z)] = Cube3D((x, y, z), False)

        for y in self.y_vals:
            for x in range(self.x_vals[0], self.x_vals[1] + 1):
                for z in range(self.z_vals[0], self.z_vals[1] + 1):
                    self.current_cubes[(x, y, z)] = Cube3D((x, y, z), False)

        for z in self.z_vals:
            for x in range(self.x_vals[0], self.x_vals[1] + 1):
                for y in range(self.y_vals[0], self.y_vals[1] + 1):
                    self.current_cubes[(x, y, z)] = Cube3D((x, y, z), False)


    def simulate_one_iteration(self):
        self.expand_board()

        updated_dict = deepcopy(self.current_cubes)

        for pos in self.current_cubes:
            if self.current_cubes[pos].active:
                if sum([neighbor.active for neighbor in self.get_neighboring_cubes(pos)]) not in (2, 3):
                    updated_dict[pos].active = False
            else:
                if sum([neighbor.active for neighbor in self.get_neighboring_cubes(pos)]) == 3:
                    updated_dict[pos].active = True

        self.current_cubes = updated_dict

    def __str__(self):
        return_str = ""

        for z in range(self.z_vals[0], self.z_vals[1] + 1):
            current = ""

            for y in range(self.y_vals[0], self.y_vals[1] + 1):
                for x in range(self.x_vals[0], self.x_vals[1] + 1):

                    current += "#" if self.current_cubes[(x,y,z)].active else "."
                current += '\n'

            return_str += f"\n{current}\n"
        return return_str

    def __repr__(self):
        return self.__str__()

    def simulate(self):
        for i in range(6):
            self.simulate_one_iteration()

            with open("storage.txt", "a") as f:
                current = ""

                for y in range(self.y_vals[0], self.y_vals[1] + 1):
                    for x in range(self.x_vals[0], self.x_vals[1] + 1):
                        current += "#" if self.current_cubes[(x, y, 0)].active else "."
                    current += '\n'

                f.write(current + '\n')

        print(sum([cube.active for cube in self.current_cubes.values()]))

class Cube4D:
    def __init__(self, position: Tuple[int, int, int, int], active: bool): # position = x, y, z
        self.position = position
        self.active = active
    def __str__(self):
        return f"Cube({self.position}, {self.active})"
    def __repr__(self):
        return self.__str__()

class Dimention4D:
    def __init__(self, inpt):
        self.current_cubes: Dict[Tuple[int, int, int, int]: Cube4D] = {(x, y, 0, 0): Cube4D((x, y, 0, 0), cube == "#") for y, row in enumerate(inpt) for x, cube in enumerate(row)}

        self.x_vals = [0, len(inpt[0])-1] # Gives the range of x/y/z values, both are INCLUSIVE
        self.y_vals = [0, len(inpt)-1]
        self.z_vals = [0, 0]
        self.w_vals = [0, 0]

    def get_neighboring_cubes(self, position: Tuple[int, int, int, int]) -> set:
        return_cubes = set()
        x, y, z, w = position

        shifts = (-1, 0, 1)

        for x_change in shifts:
            for y_change in shifts:
                for z_change in shifts:
                    for w_change in shifts:
                        if x_change == y_change == z_change == w_change == 0:
                            continue
                        else:
                            try:
                                return_cubes.add(self.current_cubes[(x+x_change, y+y_change, z+z_change, w+w_change)])
                            except KeyError:
                                pass

        return return_cubes

    def expand_board(self):
        self.x_vals[0], self.x_vals[1] = self.x_vals[0] - 1, self.x_vals[1] + 1
        self.y_vals[0], self.y_vals[1] = self.y_vals[0] - 1, self.y_vals[1] + 1
        self.z_vals[0], self.z_vals[1] = self.z_vals[0] - 1, self.z_vals[1] + 1
        self.w_vals[0], self.w_vals[1] = self.w_vals[0] - 1, self.w_vals[1] + 1


        for x in self.x_vals:
            for y in range(self.y_vals[0], self.y_vals[1] + 1):
                for z in range(self.z_vals[0], self.z_vals[1] + 1):
                    for w in range(self.w_vals[0], self.w_vals[1] +1):
                        self.current_cubes[(x, y, z, w)] = Cube4D((x, y, z, w), False)

        for y in self.y_vals:
            for x in range(self.x_vals[0], self.x_vals[1] + 1):
                for z in range(self.z_vals[0], self.z_vals[1] + 1):
                    for w in range(self.w_vals[0], self.w_vals[1] + 1):
                        self.current_cubes[(x, y, z, w)] = Cube4D((x, y, z, w), False)

        for z in self.z_vals:
            for x in range(self.x_vals[0], self.x_vals[1] + 1):
                for y in range(self.y_vals[0], self.y_vals[1] + 1):
                    for w in range(self.w_vals[0], self.w_vals[1] + 1):
                        self.current_cubes[(x, y, z, w)] = Cube4D((x, y, z, w), False)

        for w in self.w_vals:
            for x in range(self.x_vals[0], self.x_vals[1] + 1):
                for y in range(self.y_vals[0], self.y_vals[1] + 1):
                    for z in range(self.z_vals[0], self.z_vals[1] + 1):
                        self.current_cubes[(x, y, z, w)] = Cube4D((x, y, z, w), False)


    def simulate_one_iteration(self):
        self.expand_board()

        updated_dict = deepcopy(self.current_cubes)

        for pos in self.current_cubes:
            if self.current_cubes[pos].active:
                if sum([neighbor.active for neighbor in self.get_neighboring_cubes(pos)]) not in (2, 3):
                    updated_dict[pos].active = False
            else:
                if sum([neighbor.active for neighbor in self.get_neighboring_cubes(pos)]) == 3:
                    updated_dict[pos].active = True

        self.current_cubes = updated_dict

    def __str__(self):
        return_str = ""

        for w in range(self.w_vals[0], self.w_vals[1]+1):
            for z in range(self.z_vals[0], self.z_vals[1] + 1):
                current = ""

                for y in range(self.y_vals[0], self.y_vals[1] + 1):
                    for x in range(self.x_vals[0], self.x_vals[1] + 1):
                        current += "#" if self.current_cubes[(x,y,z,w)].active else "."
                    current += '\n'

                return_str += f"z={z}, w={w}\n{current}\n"
        return return_str

    def __repr__(self):
        return self.__str__()

    def simulate(self):
        for i in range(6):
            self.simulate_one_iteration()

        print(sum([cube.active for cube in self.current_cubes.values()]))

# dimention3D = Dimention3D(inpt)
# dimention3D.simulate()
# print(dimention3D)
# dimention4D = Dimention4D(inpt)
# dimention4D.simulate()

# print(sum([eval(a.replace(" + ", "*").replace(" * ", "+")) for a in open("input.txt").read().split("\n")]))