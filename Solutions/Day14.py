inpt = open("input.txt").read().split("\n")

current_mask = ["X" for i in range(36)]
mem = {}


for i in inpt:
    if "mask" in i:
        current_mask = list(i.split(" = ")[1])
        continue

    write_pos = int(i[i.index("[")+1:i.index("]")])
    num = list(str(bin(int(i.split(" = ")[1])))[2:])

    n_len = len(num)
    mask_len = len(current_mask)

    result = ["0" for d in range(mask_len)]

    for j in range(n_len):
        result[mask_len-j-1] = num[n_len-j-1]


    for j in range(mask_len):
        if current_mask[j] != "X":
            result[j] = current_mask[j]

    mem[write_pos] = int("".join(map(str, result)), 2)

print(sum(map(lambda x: mem[x], mem)))

mem = {}

def write_to_mem(num, index, writing, val):
    if index == len(num) -1:
        global mem

        if num[index] != "X":
            mem[int(writing + num[index], 2)] = val
        else:
            mem[int(writing + "1", 2)] = val
            mem[int(writing + "0", 2)] = val
        return
    if num[index] != "X":
        write_to_mem(num, index+1, writing+num[index], val)
    else:
        write_to_mem(num, index+1, writing+"1", val)
        write_to_mem(num, index + 1, writing + "0", val)

for i in inpt:
    if "mask" in i:
        if "mask" in i:
            current_mask = list(i.split(" = ")[1])
            continue

    write_pos = list(str(bin(int(i[i.index("[") + 1:i.index("]")])))[2:])
    num = int(i.split(" = ")[1])

    n_len = len(write_pos)
    mask_len = len(current_mask)

    result = ["0" for d in range(mask_len)]

    for j in range(n_len):
        result[mask_len-j-1] = write_pos[n_len-j-1]

    for j in range(mask_len):
        if current_mask[j] != "0":
            result[j] = current_mask[j]

    write_to_mem("".join(result), 0, "", num)

print(sum(map(lambda x: mem[x], mem)))