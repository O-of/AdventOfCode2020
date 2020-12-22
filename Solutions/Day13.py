# inpt = open("input.txt").read().strip().split()
#
# earliest_time = int(inpt[0])
# bus_times = list(map(int, [i for i in inpt[1].split(",") if i != "x"]))
#
# x = {}
#
# for i in bus_times:
#     x[i] = (earliest_time // i + 1) * i
#
# min_bus = 0
# min_time = 1000000000000000000000000000000
#
# for i in x:
#     if x[i] < min_time:
#         min_bus  = i
#         min_time = x[i]
#
# print(min_bus * (min_time - earliest_time))
#
# # No, part 2 will not work
# bus_times = [int(i) if i != "x" else i for i in inpt[1].split(',')]
# bus_indexs = {i:bus_times[i] for i in range(len(bus_times)) if bus_times[i] != "x"}
#
# x = 0
# l = len(bus_times)
#
# while True:
#     for i in bus_indexs:
#         if (x+i) % bus_indexs[i] != 0:
#             break
#     else:
#         print(x)
#         input()
#     x += 29

# inpt = open("input.txt").read().strip().split()
# bus_times = [int(i) if i != "x" else i for i in inpt[1].split(',')]
# bus_indexs = {i:bus_times[i] for i in range(len(bus_times)) if bus_times[i] != "x"}
#
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
# def crt(num1, mod1, num2, mod2):
#     l = lcm(mod1, mod2)
#
#     if gcd(mod1, mod2) != 1 and num1 % l != num2 % l:
#
#         raise Exception
#
#     for i in range(l):
#         if i % mod1 == (mod1+num1) % mod1 and i % mod2 == (mod2+num2) % mod2:
#             return i, lcm(mod1, mod2)
#
#     print(num1)
#     print(mod1)
#     print(num2)
#     print(mod2)
#
#     raise Exception
#
# current = (0, bus_indexs[0])
#
# for i in bus_indexs:
#     current = crt(*current, -i, bus_indexs[i])
#     print(current)

bus_indexs = {o:int(n) for o, n in enumerate(open("input.txt").read().split()[1].split(",")) if n != "x"}

working_nums = set()
current_num = 0
increment = 1


while True:
    temp_nums = set()
    for offset in bus_indexs:
        if (current_num + offset) % bus_indexs[offset] == 0:
            temp_nums.add(bus_indexs[offset])
        else:
            break

    if len(temp_nums) > len(working_nums):
        working_nums = temp_nums
        increment = __import__("functools").reduce(lambda x,y: x*y, working_nums)

    if len(working_nums) == 9:
        break

    current_num += increment

print(current_num)