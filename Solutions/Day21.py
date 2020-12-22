inpt = open("input.txt").read().split('\n')

foods_to_allergens = {food.split(" (")[0]: food.split(" (contains ")[1][0:-1].split(", ") for food in inpt}
# foods_containing_none = {ingredient for food in foods_to_allergens for ingredient in food.split()}

# keys = list(foods_to_allergens.keys())

# for i in range(len(keys)):
#     for j in range(i+1, len(keys)):
#         for ingredient in set(keys[i].split()).intersection(set(keys[j].split())):
#             try:
#                 foods_containing_none.remove(ingredient)
#             except KeyError:
#                 pass

all_foods = {ingredient for food in foods_to_allergens for ingredient in food.split()}

allergens_possibles = {allergen: all_foods.copy() for food in foods_to_allergens for allergen in foods_to_allergens[food]}

for food in foods_to_allergens:
    for allergen in foods_to_allergens[food]:
        allergens_possibles[allergen] = allergens_possibles[allergen].intersection(set(food.split()))

changed = True
while changed:
    changed = False

    for allergen in allergens_possibles:
        if isinstance(allergens_possibles[allergen], set):
            if len(allergens_possibles[allergen]) == 1:
                ingredient = next(iter(allergens_possibles[allergen]))
                allergens_possibles[allergen] = ingredient
                changed = True

                for i in allergens_possibles:
                    try:
                        allergens_possibles[i].remove(ingredient)
                    except KeyError:
                        pass
                    except AttributeError:
                        pass


# print(len({ingredient for food in foods_to_allergens for ingredient in food.split()}) - len(set().union(*allergens_possibles.values())))
foods_containing_allergens = set()
# j for i in allergens_possibles for j in allergens_possibles[i]
for i in allergens_possibles:
    if isinstance(allergens_possibles[i], set):
        for j in allergens_possibles[i]:
            foods_containing_allergens.add(j)
    else:
        foods_containing_allergens.add(allergens_possibles[i])

# print(foods_containing_allergens)
all_foods_no_allergens = all_foods.difference(foods_containing_allergens)

# print(allergens_possibles)

tally = 0
for f in foods_to_allergens:
    for i in f.split():
        if i in all_foods_no_allergens:
            tally += 1
print(tally)

print(",".join([allergens_possibles[i] for i in sorted(allergens_possibles)]))
