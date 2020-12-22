# inpt = list(map(int, open("input.txt").read().strip().split("\n")))
# inpt.append(0)
# inpt.append(max(inpt) + 3)
#
# inpt.sort()
#
# one_dif = 0
# three_dif = 0
#
# for i in range(len(inpt)-1):
#     if inpt[i+1] - inpt[i] == 1:
#         one_dif += 1
#     elif inpt[i+1] - inpt[i] == 3:
#         three_dif += 1
#
# print(one_dif * three_dif)
#
# possibles = {}
# for i in range(len(inpt)):
#     ad = 1
#     possible = []
#     num = inpt[i]
#
#     try:
#         while inpt[i+ad] - num<= 3:
#             possible.append(inpt[i+ad])
#             ad += 1
#     except Exception:
#         pass
#
#     possibles[num] = possible
# #
# def find_nums(num):
#     if num == 167:
#         return 1
#
#     results = possibles[num]
#     total = 0
#
#     for i in results:
#         total += find_nums(i)
#
#     return total
#
# a = list(possibles)
# a.sort(reverse=True)
# b = {i:0 for i in a}
#
# b[a[0]] = 1
#
# for i in a[1:]:
#     b[i] = sum([b[n] for n in possibles[i]])
#
# print(b[0])

# print([p.count(1)*p.count(3) for p in [[i[j+1]-i[j] for i in [[x.extend((0, max(x)+3)),x.sort(),x][2] for x in [list(map(int,open("input.txt").read().split()))]] for j in range(len(i)-1)]]][0])
# print([adapters for adapters in sorted(map(int,open("input.txt").read().split()), reverse=True)])
# print([[cache.setdefault(adapter, (1, sum([cache[num] for num in adapters if 0<num-adapter<4]))[bool(len(cache))]), cache][1] for cache in [{}] for adapters in [[x.extend((0, max(x)+3)),x.sort(reverse=True),x][2] for x in [list(map(int,open("input.txt").read().split()))]] for adapter in adapters][0][0])
print([[c.setdefault(b,(1,sum([c[d]for d in a if 0<d-b<4]))[bool(len(c))]),c][1]for c in[{}]for a in[[x.extend((0,max(x)+3)),x.sort(reverse=True),x][2]for x in[list(map(int,open("input.txt").read().split()))]]for b in a][0])