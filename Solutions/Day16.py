from copy import deepcopy

inpt = open("input.txt").read().split("\n\n")

constraints = list(map(lambda x: x.split(": ")[1].split(" or "), inpt[0].split('\n')))
your_ticket = list(map(int, inpt[1].split("\n")[1].split(',')))

nearby_tickets = inpt[2].split('\n')[1:]

valid_tickets = set(nearby_tickets)

total_error_rate = 0

for nearby_ticket in nearby_tickets:
    ticket_nums = list(map(int, nearby_ticket.split(",")))

    for num in ticket_nums:
        for constraint in constraints:

            con1 = list(map(int, constraint[0].split("-")))
            con2 = list(map(int, constraint[1].split("-")))


            if con1[0] <= num <= con1[1] or con2[0] <= num <= con2[1]:
                break
        else:
            total_error_rate += num
            valid_tickets.remove(nearby_ticket)
            break


name_to_constraint = {con.split(': ')[0]: con.split(": ")[1].split(" or ") for con in inpt[0].split('\n')}
possible_vals = [set(name_to_constraint.keys()) for i in range(len(name_to_constraint))]

changed = True
while changed:
    changed = False

    for ticket in valid_tickets:
        ticket_fields = list(map(int, ticket.split(",")))

        for pos, field in enumerate(ticket_fields):
            possibles = possible_vals[pos]

            for constraint in possibles.copy():
                con1 = list(map(int, name_to_constraint[constraint][0].split("-")))
                con2 = list(map(int, name_to_constraint[constraint][1].split("-")))

                if con1[0] <= field <= con1[1] or con2[0] <= field <= con2[1]:
                    continue
                else:
                    possibles.remove(constraint)
                    changed = True

    if not changed:
        for possibles in possible_vals:
            if len(possibles) == 1:
                field = next(iter(possibles))

                for possibles1 in possible_vals:
                    if possibles1 is not possibles:
                        try:
                            possibles1.remove(field)
                            changed = True
                        except Exception:
                            continue


vals = 1
count = 0

for pos, field in enumerate(possible_vals):
    f = next(iter(field))
    if "departure" in f:
        vals *= your_ticket[pos]
        count += 1

print(vals)
print(count)