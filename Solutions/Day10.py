inpt = list(map(int, open("input.txt").read().strip().split('\n')))

def find_sum(preamble, num):
    for i in range(len(preamble)):
        for j in range(i+1, len(preamble)):
            if preamble[i] + preamble[j] == num:
                return True
    return False

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

print(find_sub_array(inpt[indexes[0]]))