import time

start = time.time()

inpt_map = open("input.txt").read().split('\n')

def get_trees(right, down):
    tree_count = 0

    current_pos = [0, 0]

    while current_pos[1] < len(inpt_map):
        if inpt_map[current_pos[1]][current_pos[0]] == '#':
            tree_count += 1

        current_pos[0] = (current_pos[0] + right) % len(inpt_map[0])
        current_pos[1] += down

    return tree_count


print(get_trees(3, 1))
print(get_trees(1, 1) * get_trees(3, 1) * get_trees(5, 1) * get_trees(7, 1) * get_trees(1, 2))
print(time.time() - start)
# # 1ms ???

# print(len(list(filter(lambda y: inpt_map[y][(y * 3) % len(inpt_map[0])] == "#", range(len(inpt_map))))))
# print(sum(map(lambda y : 1 if inpt_map[y][(y * 3) % len(inpt_map[0])] == "#" else 0, range(len(inpt_map)))))

# print(sum([inpt_map[y][(y * 3) % len(inpt_map[0])] == "#" for y in range(len(inpt_map))]))