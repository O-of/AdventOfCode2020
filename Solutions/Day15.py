# inpt = open("input.txt").read().split(",")
#
# numbers_said = {0:0}
# last_turn_said = {0:[]}
# turn = 1
# max_num = 0
# last_said = None
# #
# for num in inpt:
#     if int(num) in numbers_said:
#         numbers_said[int(num)] += 1
#     else:
#         numbers_said[int(num)] = 1
#     last_turn_said[int(num)] = [turn]
#     turn += 1
#
#     max_num = max(max_num, numbers_said[int(num)])
#     last_said = int(num)
#
#     # input(f"Turn: {turn-1} Number: {last_said}")
# #
# # # while max_num < 2020:
# for i in range(2020 - len(inpt)):
#     if numbers_said[last_said] == 1:
#         last_said = 0
#         numbers_said[0] += 1
#         last_turn_said[0].append(turn)
#
#     elif last_said in numbers_said:
#         last_said = last_turn_said[last_said][-1] - last_turn_said[last_said][-2]
#
#         if last_said in numbers_said:
#             numbers_said[last_said] += 1
#             last_turn_said[last_said].append(turn)
#         else:
#             numbers_said[last_said] = 1
#             last_turn_said[last_said] = [turn]
#
#     else:
#         numbers_said[last_said] = 1
#         last_turn_said[last_said] = [turn]
#
#     turn += 1
#     max_num = max(max_num, numbers_said[last_said])
#
#     # input(f"Turn: {turn-1} Number: {last_said}")
#
# print(last_said)
# print(turn)

inpt = open("input.txt").read().split(",")
num_to_turn = {int(num): [turn + 1] for turn, num in enumerate(inpt)}
last_num_said = int(inpt[-1])

nums = [last_num_said]

for turn in range(len(num_to_turn) + 1, 30_000_000 + 1):
    if len(num_to_turn[last_num_said]) < 2:
        last_num_said = 0
    else:
        last_num_said = num_to_turn[last_num_said][-1] - num_to_turn[last_num_said][-2]

    num_to_turn.setdefault(last_num_said, [])
    num_to_turn[last_num_said].append(turn)

    if turn % 100_000 == 0:
        print(f"Turn: {turn} Last Number: {last_num_said}")

    if turn % 1000 == 0:
        nums.append(last_num_said)

from matplotlib import pyplot as plt
plt.plot(nums)
plt.show()