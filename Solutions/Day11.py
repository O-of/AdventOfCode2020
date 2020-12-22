# # from copy import deepcopy
# #
# # inpt = open("input.txt").read().split()
# # board = list(map(lambda x: list(x), inpt))
# #
# # def find_num_seats(row, column):
# #     total = 0
# #
# #     for r in (-1, 0, 1):
# #         for c in (-1, 0, 1):
# #             if r == 0 and c == 0:
# #                 continue
# #
# #             mult = 1
# #
# #             while 0 <= r*mult + row < len(inpt) and 0 <= c*mult + column < len(inpt[0]):
# #                 # print(r * mult + row, c * mult + column)
# #                 # print(row, column)
# #                 if board[r*mult + row][c*mult + column] == "#":
# #                     total += 1
# #                     break
# #                 elif board[r*mult + row][c*mult + column] == "L":
# #                     break
# #                 else:
# #                     mult += 1
# #
# #     return total
# #
# # old_board = deepcopy(board)
# #
# # changed = True
# #
# #
# # while changed:
# #     changed = False
# #
# #     for row in range(len(inpt)):
# #         for column in range(len(inpt[0])):
# #             if board[row][column] == "L":
# #                 total = find_num_seats(row, column)
# #                 if total == 0:
# #                     changed = True
# #                     old_board[row][column] = "#"
# #
# #             elif board[row][column] == "#":
# #                 total = find_num_seats(row, column)
# #                 if total >= 5:
# #                     changed = True
# #                     old_board[row][column] = "L"
# #
# #     # print(old_board)
# #     board = deepcopy(old_board)
# #
# # t = 0
# # for row in board:
# #     t += row.count("#")
# # print(t)
# # print(board)
#
# from copy import deepcopy
# min_people = 4 # 5 for part 2, 4 for part 1
#
#
# inpt = list(map(list, open("input.txt").read().split()))
#
# def find_seats_p1():
#     coord_to_seats = {}
#
#     for row in range(len(inpt)):
#         for column in range(len(inpt[0])):
#             seats = []
#
#             for r in (-1, 0, 1):
#                 for c in (-1, 0, 1):
#                     if r == 0 and c == 0:
#                         continue
#
#                     if 0 <= r + row < len(inpt) and 0 <= c + column < len(inpt[0]):
#                         if inpt[r + row][c  + column] in ("#", "L"):
#                             seats.append((r + row, c + column))
#
#             coord_to_seats[(row, column)] = seats
#
#     return coord_to_seats
#
# def find_seats_p2():
#     coord_to_seats = {}
#
#     for row in range(len(inpt)):
#         for column in range(len(inpt[0])):
#             seats = []
#
#             for r in (-1, 0, 1):
#                 for c in (-1, 0, 1):
#                     if r == 0 and c == 0:
#                         continue
#
#                     mult = 1
#
#                     while 0 <= r * mult + row < len(inpt) and 0 <= c * mult + column < len(inpt[0]):
#                         if inpt[r * mult + row][c * mult + column] in ("#", "L"):
#                             seats.append((r * mult + row, c * mult + column))
#                             break
#                         else:
#                             mult += 1
#
#             coord_to_seats[(row, column)] = seats
#
#     return coord_to_seats
#
# def find_occupied(visible):
#     return len([1 for coord in visible if inpt[coord[0]][coord[1]] == "#"])
#
# results = find_seats_p1()
#
# inpt_modify = deepcopy(inpt)
# changed = True
#
# i = 0
#
# while changed:
#     i += 1
#     changed = False
#
#     for coord in results:
#         row, col = coord
#
#         if inpt[row][col] == "L":
#             if find_occupied(results[coord]) == 0:
#                 inpt_modify[row][col] = "#"
#                 changed = True
#         elif inpt[row][col] == "#":
#             if find_occupied(results[coord]) >= min_people:
#                 inpt_modify[row][col] = "L"
#                 changed = True
#
#     inpt = deepcopy(inpt_modify)
#
# print(sum([row.count("#") for row in inpt]))
# print(i)

print([[board_copy[row].pop(col), board_copy[row].insert(col, ("L", "#")[len(total) == 0]), board_copy][2] for queue in [[list(map(lambda x: list(x), open("input.txt").read().split()))]] for board in queue for board_copy in [__import__("copy").copy(board)] for changed in [[False]] for row in range(len(board)) for col in range(len(board[0])) for total in [[1 for r_shift in (-1, 0, 1) for c_shift in (-1, 0, 1) if not r_shift == c_shift == 0 if 0 <= r_shift + row < len(board) and 0 <= c_shift + col < len(board[0]) if board[r_shift + row][c_shift + col] == "#"]] if (board[row][col] == "L" and len(total) == 0) or (board[row][col] == "#" and len(total) >= 4)][-1])