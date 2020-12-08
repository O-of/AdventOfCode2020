# inpt = open("input.txt", "r").read().split("\n")
#
# highest = 0
# ids = []
#
# for b_pass in inpt:
#     acceptable = list(range(128))
#     for i in range(7):
#         part = b_pass[i]
#         if part == "F":
#             acceptable = acceptable[:len(acceptable) // 2]
#         elif part == "B":
#             acceptable = acceptable[len(acceptable) // 2:]
#         else:
#             print(part)
#
#     row = acceptable[0]
#
#     acceptable = list(range(8))
#     for i in range(3):
#         part = b_pass[7 + i]
#         if part == "L":
#             acceptable = acceptable[:len(acceptable) // 2]
#         elif part == "R":
#             acceptable = acceptable[len(acceptable) // 2:]
#         else:
#             print(part)
#
#     column = acceptable[0]
#
#     # if row * 8 + column > highest:
#     #     highest = row * 8 + column
#     ids.append(row * 8 + column)
#     ids.sort()
#
# # print(ids)
# for i in range(27, 963):
#     if i not in ids:
#         print(i)
# # print(ids)

ids = [sum([2 ** (6 - i) for i in range(7) if b_pass[i] == "B"]) * 8 + sum([2 ** (2 - i) for i in range(3) if b_pass[7 + i] == "R"]) for b_pass in open("input.txt", "r").read().split("\n")]
print(max(ids))
print(list(filter(lambda x: x not in ids,range(27, 963)))[0])