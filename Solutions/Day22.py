inpt = open("input.txt").read().strip().split("\n\n")


player1 = list(map(int, inpt[0].split('\n')[1:]))
player2 = list(map(int, inpt[1].split('\n')[1:]))

def part1(deck1, deck2):
    player1 = deck1.copy()
    player2 = deck2.copy()

    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    t = 0
    for i, j in enumerate(player1):
        t += (50-i) * int(j)
    print(t)

def recursive_combat(deck1, deck2):
    previous_games = set() # will be tuple(player1, player2)

    player1 = deck1.copy()
    player2 = deck2.copy()

    winner = None
    while not winner:
        if (tuple(player1), tuple(player2)) in previous_games:
            winner = "p1"
        else:
            previous_games.add((tuple(player1), tuple(player2)))

            card1 = player1.pop(0)
            card2 = player2.pop(0)

            if card1 <= len(player1) and card2 <= len(player2):
                result = recursive_combat(player1[:card1], player2[:card2])[0]

                if result == "p1":
                    player1.append(card1)
                    player1.append(card2)
                else:
                    player2.append(card2)
                    player2.append(card1)
            else:
                if card1 > card2:
                    player1.append(card1)
                    player1.append(card2)
                else:
                    player2.append(card2)
                    player2.append(card1)

            if len(player1) == 0:
                winner = "p2"
            elif len(player2) == 0:
                winner = "p1"

    return winner, player1, player2

def part2(player1, player2):
    result = recursive_combat(player1, player2)
    if result[0] == "p1":
        winner = result[1]
    else:
        winner = result[2]

    t = 0

    for i, j in enumerate(winner):
        t += (50 - i) * int(j)

    print(t)

part1(player1, player2)
part2(player1, player2)