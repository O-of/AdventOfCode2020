from typing import List
import time

start = time.time()

class CodeGenerator(object):
    def __init__(self, inpt: List[str]):
        self.inpt = inpt

    def generate_outputs(self):
        yield self.inpt

        for i in range(len(self.inpt)):
            copy_inpt = self.inpt.copy()

            instruction = self.inpt[i].split()

            func = instruction[0]
            value = instruction[1]

            if func == "nop":
                copy_inpt[i] = f"jmp {value}"
            elif func == "jmp":
                copy_inpt[i] = f"nop {value}"
            else:
                continue

            yield copy_inpt


class BootCodeRunner(object):
    def __init__(self, inpt: List[str]):
        self.inpt = inpt

        self.accumulator = 0
        self.instruction_pointer = 0

        self.visited_locations = set()

    def reassign_inpt(self, inpt: List[str]):
        self.inpt = inpt

        self.accumulator = 0
        self.instruction_pointer = 0

        self.visited_locations = set()

    def acc(self, increment: int):
        self.accumulator += increment
        self.instruction_pointer += 1

    def jmp(self, spaces: int):
        self.instruction_pointer += spaces

    def nop(self):
        self.instruction_pointer += 1

    def run_code(self):
        while self.instruction_pointer < len(self.inpt):
            if self.instruction_pointer in self.visited_locations:
                return False
            else:
                self.visited_locations.add(self.instruction_pointer)

            instruction = self.inpt[self.instruction_pointer].split()

            func = instruction[0]
            value = int(instruction[1])

            if func == "acc":
                self.acc(value)
            elif func == "jmp":
                self.jmp(value)
            elif func == "nop":
                self.nop()

        print(self.accumulator)
        return True


class BootLoader(object):
    def __init__(self, inpt: List[str]):
        self.inpt = inpt
        self.code_generators = CodeGenerator(inpt)

    def run_code(self):
        boot_loader_runner = BootCodeRunner([])

        for inpt in self.code_generators.generate_outputs():
            boot_loader_runner.reassign_inpt(inpt)
            result = boot_loader_runner.run_code()

            if result:
                break

loader = BootLoader(open("input.txt").read().strip().split('\n'))
loader.run_code()

print(time.time() - start)
# # 41 ms