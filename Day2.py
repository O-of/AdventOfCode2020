inpt_password = list(map(lambda x: x.split(': '), open("input.txt", "r").read().split("\n")))
inpt_password = [[i[0].split(" "), i[1]] for i in inpt_password]
inpt_password = [[[i[0][0].split('-'), i[0][1]], i[1]] for i in inpt_password]

valid_passowrds = 0

# for i in inpt_password:
#     password = i[1]
#     letter = i[0][1]
#     min = int(i[0][0][0])
#     max = int(i[0][0][1])
#
#     if min <= password.count(letter) <= max:
#         valid_passowrds += 1

for i in inpt_password:
    password = i[1]
    letter = i[0][1]
    pos1 = int(i[0][0][0]) - 1
    pos2 = int(i[0][0][1]) - 1

    count = 0
    if password[pos1] == letter:
        count += 1
    if password[pos2] == letter:
        count += 1

    if count == 1:
        valid_passowrds += 1

print(valid_passowrds)
