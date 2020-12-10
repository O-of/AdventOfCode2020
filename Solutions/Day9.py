import time
start = time.time()

inpt = list(map(int, open("input.txt").read().strip().split('\n')))

def find_sum(preamble, num):
    for i in range(len(preamble)):
        for j in range(i+1, len(preamble)):
            if preamble[i] + preamble[j] == num:
                return True
    return False

# [preamble[i] + preamble[j] == num for i in range(len(preamble)) for j in range(i+1, len(preamble))]



# print([inpt[i] for inpt in (list(map(int, open("input.txt").read().strip().split('\n'))),) for i in range(25, len(inpt)) for preamble in (inpt[i-25:i],) if sum([preamble[j] + preamble[k] == inpt[i] for j in range(25) for k in range(j+1, 25)]) == 0][0])
# print([[(preamble[j], preamble[k]) for j in range(25) for k in range(j+1, 25) if preamble[j] + preamble[k] == inpt[i]] for inpt in (list(map(int, open("input.txt").read().strip().split('\n'))),) for i in range(25, len(inpt)) for preamble in (inpt[i-25:i],)][0])

indexes = []

for i in range(25, len(inpt)):
    if not find_sum(inpt[i-25:i] , inpt[i]):
        indexes.append(i)

def find_sub_array(total):
    possibles = []

    for i in range(len(inpt)):
        s = inpt[i]
        k = i

        for j in range(i, len(inpt)-1):
            k += 1
            s += inpt[k]

            if s == total:
                possibles.append((inpt[i], inpt[k]))
            elif s > total:
                break
    return possibles

print(inpt[indexes[0]])
arr = find_sub_array(inpt[indexes[0]])

print(arr[0][0] + arr[0][-1])
print(time.time() - start)
# # 24 ms