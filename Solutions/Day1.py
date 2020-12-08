inpt_text = list(map(int, open("input.txt").read().split("\n")))

def part1(inpt):
    for n1 in range(len(inpt)):
        for n2 in range(n1 + 1, len(inpt)):
            if inpt[n1] + inpt[n2] == 2020:
                print(inpt[n1] * inpt[n2])

def part2(inpt):
    for n1 in range(len(inpt)):
        for n2 in range(n1 + 1, len(inpt)):
            for n3 in range(n2 + 1, len(inpt)):
                if inpt[n1] + inpt[n2] + inpt[n3] == 2020:
                    print(inpt[n1] * inpt[n2] * inpt[n3])

# part2(inpt_text)

print([inpt_text[n1] * inpt_text[n2] for n1 in range(len(inpt_text)) for n2 in range(n1 + 1, len(inpt_text)) if inpt_text[n1] + inpt_text[n2] == 2020][0])
print([inpt_text[n1] * inpt_text[n2] * inpt_text[n3] for n1 in range(len(inpt_text)) for n2 in range(n1 + 1, len(inpt_text)) for n3 in range(n2 + 1, len(inpt_text)) if inpt_text[n1] + inpt_text[n2] + inpt_text[n3] == 2020][0])