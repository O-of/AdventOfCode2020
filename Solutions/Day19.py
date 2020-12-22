from functools import lru_cache
import time

start = time.time()

inpt = open("input.txt").read().split("\n\n")

rules = {}
temp_rules = {rule.split(": ")[0]: rule.split(": ")[1].split(" | ") for rule in inpt[0].split("\n")}
messages = inpt[1].split("\n")

@lru_cache()
def make_rules(rule_num):
    sub_rules = temp_rules[rule_num]
    return_rules = []

    if '"' in sub_rules[0]:
        return [sub_rules[0][1]]
    else:
        for sub in sub_rules:
            r1 = list(map(lambda x: make_rules(x), sub.split(" ")))
            return_rules.extend(create_permutations(r1))

            # for r in r1:
            #     string = r
            # r1 = sub.split(" ")[0]
            # r2 = sub.split(" ")[1]

            # for val1 in make_rules(r1):
            #     for val2 in make_rules(r2):
            #         return_rules.append(val1+val2)

        return return_rules

def create_permutations(l):
    if len(l) == 1:
        return l[0]
    else:
        perms = []
        for a in l[0]:
            for b in create_permutations(l[1:]):
                perms.append(a+b)
        return perms

# possibles = set(make_rules("0"))
# total = 0

f2 = set(make_rules("42"))
t1 = set(make_rules("31"))

print(f2)
print(t1)

first = True
total = 0

for i in messages:
    t = list(map(''.join, zip(*[iter(i)]*len(next(iter(f2))))))
    count_first = 0
    count_second = 0

    for p in t:
        if p in f2 and count_second == 0:
             count_first += 1
        elif p in t1:
            count_second += 1
        else:
            break
    else:
        
        if count_first > 1 and count_second > 0 and count_second < count_first and count_second + count_first == len(t) and len(t):
            total += 1

    # first = True
    # good = True
    # current = 0
    #
    # num_f = 0
    # num_s = 0
    #
    # while current < len(i):
    #     if first:
    #         if i[current:current+len(next(iter(f2)))] in f2:
    #             num_f += 1
    #             current += len(next(iter(f2)))
    #         else:
    #             first = False
    #     else:
    #         if i[current:current+len(next(iter(f2)))] in t1:
    #             num_s += 1
    #             current += len(next(iter(f2)))
    #         else:
    #             good = False
    #             break
    #
    # if good and num_f > 1 and num_s > 0:
    #     total += 1
    #
    #     print(i)
    #     print(num_f)
    #     print(num_s)

print(total)
print(time.time() - start)

# for i in messages:
#     if i in possibles:
#         total += 1
# print(total)

# print(make_rules("0"))