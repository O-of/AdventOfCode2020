# inpt = []

# with open("input.txt", "r") as f:
#     current_s = ""
#     for i in f:
#         if i != "\n":
#             current_s += i.replace("\n", "")
#         else:
#             inpt.append(current_s)
#             current_s = ""
#     inpt.append(current_s)

# print(inpt)

inpt = open("input.txt", "r").read().split('\n\n')
# inpt = list(map(lambda x: x.replace("\n", " "), inpt))

good = []
total = 0

for passport in inpt:
    required_fields = "byr iyr eyr hgt hcl ecl pid".split(" ")
    for i in required_fields:
        if i not in passport:
            break
    else:
        good.append(passport)
        # things = passport.split(" ")
        # d = {i.split(':')[0]: i.split(':')[1] for i in things}
        #
        # if 1920 <= int(d["byr"]) <= 2002:
        #     if 2010 <= int(d["iyr"]) <= 2020:
        #         if 2020 <= int(d["eyr"]) <= 2030:
        #             x = False
        #             if ("cm" in d["hgt"]):
        #                 if 150 <= int(d["hgt"].replace("cm", "")) <= 193:
        #                     x = True
        #             elif ("in" in d["hgt"]):
        #                 if (59 <= int(d["hgt"].replace("in", ""))) <= 76:
        #                     x = True
        #
        #             if x:
        #                 valids = "0123456789abcdef"
        #                 color = d["hcl"][1:]
        #
        #                 if len(color) != 6:
        #                     continue
        #
        #                 for z in color:
        #                     if z not in valids:
        #                         break
        #                 else:
        #                     valids = ["amb", "blu", "brn" < "gry", "grn", "hzl", "oth"]
        #                     if d["ecl"] in valids:
        #                         if len(d["pid"]) == 9:
        #                             total += 1


for passport in good:
    values = {p.split(':')[0] : p.split(':')[1] for p in passport.split()}

    if not (1920 <= int(values["byr"]) <= 2002):
        continue

    if not(2010 <= int(values["iyr"]) <= 2020):
        continue

    if not (2020 <= int(values["eyr"]) <= 2030):
        continue

    if "cm" in values["hgt"]:
        if not (150 <= int(values["hgt"].replace("cm", "")) <= 193):
            continue
    else:
        try:
            if not (59 <= int(values["hgt"].replace("in", "")) <= 76):
                continue
        except Exception:
            continue

    valid_char = "1234567890abcdef"
    if len(values["hcl"]) != 7:
        continue
    for c in (values["hcl"][1:]):
        if c not in valid_char:
            continue

    valid_color = "amb blu brn gry grn hzl oth"
    if values["ecl"] not in valid_color:
        print(values["ecl"])
        continue

    if len(values["pid"]) != 9:
        continue

    try:
        int(values["pid"])
    except Exception:
        continue

    total += 1


print(len(good))
print(total)