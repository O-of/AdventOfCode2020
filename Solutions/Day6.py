import time
start = time.time()

inpt = open("input.txt", "r").read().split("\n\n")

grousp = []

# print(sum(len(set(list(i.replace("\n", "")))) for i in open("input.txt").read().split("\n\n")))
# print([i.split() for i in open("input.txt", "r").read().split("\n\n") for a in i.split()[0]])
# print(sum(sum(a in p for p in i.split()) == len(i.split()) for i in open("input.txt").read().split("\n\n") for a in i.split()[0]))


for i in inpt:
    a = set()
    for b in i:
        if b != '\n':
            a.add(b)
    grousp.append(a)

print(sum(map(lambda x: len(x), grousp)))

t = 0

for i in inpt:
    ppl = i.split()
    keys = {}
    for p in ppl:
        for a in p:
            if a in keys:
                keys[a] += 1
            else:
                keys[a] = 1
    for k in keys:
        if keys[k] == len(ppl):
            t += 1

print(t)
print(time.time()-start)
# # 11 ms