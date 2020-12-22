import turtle
wn = turtle.Screen()
ship = turtle.Turtle()
wp = turtle.Turtle()

wn.bgcolor("light blue")
ship.speed(0)
wp.speed(0)
wp.shape("circle")
wp.color("green")
wp.pu()
wp.shapesize(0.3, 0.3, 0.3)
# ship.ht()


inpt = open("input.txt").read().strip().split()

# current_pos = [0, 0] # x y
# facing_dir = "E"
#
# for d in inpt:
#     l = d[0]
#     movements = int(d[1:])
#
#
#     if l == "N":
#         current_pos[1] += movements
#     elif l == "S":
#         current_pos[1] -= movements
#     elif l == "E":
#         current_pos[0] += movements
#     elif l == "W":
#         current_pos[0] -= movements
#     elif l == "L":
#         pos_moved = movements // 90
#         facing_dir = ("N", "W", "S", "E")[(("N", "W", "S", "E").index(facing_dir) + pos_moved) % 4]
#     elif l == "R":
#         pos_moved = movements // 90
#         facing_dir = ("N", "E", "S", "W")[(("N", "E", "S", "W").index(facing_dir) + pos_moved) % 4]
#     elif l == "F":
#         if facing_dir == "N":
#             current_pos[1] += movements
#         elif facing_dir== "S":
#             current_pos[1] -= movements
#         elif facing_dir == "E":
#             current_pos[0] += movements
#         elif facing_dir == "W":
#             current_pos[0] -= movements
#     else:
#         print(d)
#
#     ship.goto(*current_pos)
#
# print(abs(current_pos[0]) + abs(current_pos[1]))

waypoint = [10, 1]
ship_pos = [0, 0]

for d in inpt:
    l = d[0]
    movements = int(d[1:])

    if l == "N":
        waypoint[1] += movements
    elif l == "S":
        waypoint[1] -= movements
    elif l == "E":
        waypoint[0] += movements
    elif l == "W":
        waypoint[0] -= movements
    elif l == "L":
        relative_waypoint = [waypoint[0] - ship_pos[0], waypoint[1] - ship_pos[1]]

        for i in range(movements//90):
            x, y = relative_waypoint
            relative_waypoint = [-y, x]
            # x, y = waypoint
            # waypoint = [-y, x]

        waypoint = [ship_pos[0] + relative_waypoint[0], ship_pos[1] + relative_waypoint[1]]

    elif l == "R":
        relative_waypoint = [waypoint[0] - ship_pos[0], waypoint[1] - ship_pos[1]]

        for i in range(movements//90):
            x, y = relative_waypoint
            relative_waypoint = [y, -x]
            # x, y = waypoint
            # waypoint = [y, -x]

        waypoint = [ship_pos[0] + relative_waypoint[0], ship_pos[1] + relative_waypoint[1]]

    elif l == "F":
        relative_waypoint = [waypoint[0] - ship_pos[0], waypoint[1] - ship_pos[1]]

        ship_pos[0] += relative_waypoint[0] * movements
        waypoint[0] += relative_waypoint[0] * movements
        ship_pos[1] += relative_waypoint[1] * movements
        waypoint[1] += relative_waypoint[1] * movements
        # ship_pos[0] += waypoint[0] * movements
        # ship_pos[1] += waypoint[1] * movements
    else:
        print(d)

    ship.goto(*map(lambda a: a//100, ship_pos))
    wp.goto(*map(lambda a: a//100, waypoint))

print(abs(ship_pos[0]) + abs(ship_pos[1]))

wn.mainloop()