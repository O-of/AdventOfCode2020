inpt = open("input.txt").read().split("\n")

def eval_no_pemdas_one(equation):
    equation = equation.replace(" ", "")

    parentheses_locations = []

    stored_indexes = []
    parentheses_count = 0

    for i, char in enumerate(equation):
        if char == "(":
            if parentheses_count == 0:
                stored_indexes.append(i)

            parentheses_count += 1
        elif char == ")":
            parentheses_count -= 1

            if parentheses_count == 0:
                stored_indexes.append(i)

                parentheses_locations.append(tuple(stored_indexes))
                stored_indexes = []

    current_num = ""
    char_list = ["*", "+","(",")"]

    running_total = 0
    current_opterator = "+"

    i = 0
    while i < len(equation):
        char = equation[i]

        if char in char_list:
            if char == "(":
                for location in parentheses_locations:
                    if location[0] == i:
                        current_num = eval_no_pemdas(equation[location[0]+1:location[1]])
                        i = location[1]
                        break

            elif current_opterator == "+":
                running_total += int(current_num)
                current_num = ""
                current_opterator = char
            elif current_opterator == "*":
                running_total *= int(current_num)
                current_num = ""
                current_opterator = char


        else:
            try:
                current_num += char
            except:
                print(char)
                print(current_num)
                print(equation)
                input()
        i += 1

    if current_opterator == "+":
        running_total += int(current_num)
    elif current_opterator == "*":
        running_total *= int(current_num)
    return running_total

def eval_no_pemdas(equation):
    if "+" not in equation and "*" not in equation:
        return int(equation)

    parentheses_locations = []

    stored_indexes = []
    parentheses_count = 0

    for i, char in enumerate(equation):
        if char == "(":
            if parentheses_count == 0:
                stored_indexes.append(i)

            parentheses_count += 1
        elif char == ")":
            parentheses_count -= 1

            if parentheses_count == 0:
                stored_indexes.append(i)

                parentheses_locations.append(tuple(stored_indexes))
                stored_indexes = []

    temp_eq = equation
    for i in parentheses_locations:
        temp_eq = temp_eq.replace(equation[i[0]:i[1]+1], equation[i[0]:i[1]+1].replace(" ", ""))

    temp_eq = temp_eq.split(" ")
    for i in range(len(temp_eq)):
        if "(" in temp_eq[i]:
            temp_eq[i] = temp_eq[i].replace("+", " + ")
            temp_eq[i] = temp_eq[i].replace("*", " * ")

    for i in range(len(temp_eq)):
        if "(" in temp_eq[i]:
            temp_eq[i] = str(eval_no_pemdas(temp_eq[i][1:-1]))

    # equation = "".join(temp_eq)
    #
    # current_pos = 1
    #
    # while "+" in equation or "*" in equation:
    #     try:
    #         op = temp_eq[current_pos]
    #     except:
    #         print(temp_eq)
    #         print(equation)
    #         input()
    #
    #     num1 = eval_no_pemdas(temp_eq[current_pos-1])
    #     num2 = eval_no_pemdas(temp_eq[current_pos+1])
    #
    #     string = temp_eq[current_pos-1]+temp_eq[current_pos]+temp_eq[current_pos+1]
    #
    #
    #     if op == "+":
    #         result = str(num1+num2)
    #     else:
    #         result = str(num1 * num2)
    #
    #     equation = equation.replace(string, result)
    #
    #     for i in range(3):
    #         temp_eq.pop(current_pos-1)
    #     temp_eq.insert(current_pos-1, result)

    current_pos = 1
    while "+" in temp_eq:
        op = temp_eq[current_pos]

        if op == "+":
            num1 = eval_no_pemdas(temp_eq[current_pos - 1])
            num2 = eval_no_pemdas(temp_eq[current_pos + 1])

            result = str(num1 + num2)

            for i in range(3):
                temp_eq.pop(current_pos-1)
            temp_eq.insert(current_pos-1, result)

        else:
            current_pos += 2

    current_pos = 1
    while "*" in temp_eq:
        op = temp_eq[current_pos]

        if op == "*":
            num1 = eval_no_pemdas(temp_eq[current_pos - 1])
            num2 = eval_no_pemdas(temp_eq[current_pos + 1])

            result = str(num1 * num2)

            for i in range(3):
                temp_eq.pop(current_pos-1)
            temp_eq.insert(current_pos-1, result)

        else:
            current_pos += 2

    return int(temp_eq[0])

# total = 0
#
# for line in inpt:
#     try:
#         total += eval_no_pemdas(line)
#     except:
#         print(line)
#         input()
# print(total)

class MyNumber:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return MyNumber(self.num * int(other))
    def __mul__(self, other):
        return MyNumber(self.num + int(other))
    def __int__(self):
        return self.num

total = 0

for i in inpt:
    b = i.replace("(", "( ").replace(")", " )")
    c = b.split()

    for j,k in enumerate(c):
        if k.isdigit():
            c[j] = f"MyNumber({k})"

    total += int(eval(''.join(c)))

print(total)