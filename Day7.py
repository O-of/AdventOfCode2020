# inpt = open("input.txt").read().strip().split('\n')
#
# bags = {}
# for i in inpt:
#     args = i.split()
#     parts = i.split("contain ")
#     bags[f"{args[0]} {args[1]}"] = [f"{a.split()[0]} {a.split()[1]} {a.split()[2]}" for a in parts[1].split(',')]
#
# class Bag:
#     def __init__(self, a):
#         self.result = []
#         self.textures = a.split()[0]
#         self.color = a.split()[1]
#
#     def add_children(self, c, count):
#         self.result.append((c, count))
#
#     def check_gold(self):
#         if len(self.result) == 0:
#             return -1
#         if self.textures + self.color == "shiny gold":
#             return 0
#         count = -1
#         for i in self.result:
#             result = i[0].check_gold()
#             if result == -1:
#                 pass
#             elif result == 0:
#                 if count == -1:
#                     count = 0
#                 count += 1
#             else:
#                 count += result
#         return count
#
# bag_to_obj = {}
#
# bags_without_parents = [i for i in bags]
#
# for i in bags:
#     bag_to_obj[i] = Bag(i)
#
# for i in bag_to_obj:
#     for j in bags[i]:
#         if j == "no other bags.":
#             continue
#         bag_to_obj[i].add_children(bag_to_obj[f"{j.split()[1]} {j.split()[2]}"], int(j.split()[0]))
#         try:
#             bags_without_parents.pop(bags_without_parents.index(f"{j.split()[1]} {j.split()[2]}"))
#         except Exception:
#             pass
#
# print(sum([bag_to_obj[i].check_gold() for i in bags_without_parents]))
#
# # print(bags)
# #
# # old = []
# # valid_bags = ["shiny gold"]
# #
# # while len(old) != len(valid_bags):
# #
# #     # print(valid_bags)
# #
# #     old = valid_bags.copy()
# #
# #     for bag in bags:
# #         for b in bags[bag]:
# #             for v in valid_bags:
# #                 if v in b:
# #                     valid_bags.append(bag)
# #                     break
# #             else:
# #                 continue
# #             break
# #
# #
# #
# # print(len(valid_bags))

import time
start = time.time()

inpt = open("input.txt").read().strip().split("\n")


class Bag:
    def __init__(self, desc: str):
        self.desc = desc
        self.outputs = []

        self.checked = False
        self.contains_gold = False

    def add_output(self, obj: "Bag", count: int):
        self.outputs.append((obj, count))

    def check_gold(self):
        for output in self.outputs:
            if output[0].checked:
                continue

            output[0].check_gold()

        if "shiny gold" in self.desc:
            self.checked = True
            self.contains_gold = True
            return

        for output in self.outputs:
            if output[0].contains_gold:
                self.contains_gold = True
                break
        self.checked = True

    def check_num_bags(self):
        total = 0
        for result in self.outputs:
            total += result[1]
            total += result[0].check_num_bags() * result[1]
        return total


bags = {}
bag_to_obj = {}

for bag in inpt:
    original = f"{bag.split()[0]} {bag.split()[1]}"
    output = [(f"{result.split()[1]} {result.split()[2]}", result.split()[0]) for result in
              bag.split("contain ")[1].split(", ")]
    bags[original] = output

for bag in bags:
    bag_to_obj[bag] = Bag(bag)

for bag in bag_to_obj:
    results = bags[bag]
    if (results[0][0] == 'other bags.'):
        continue

    for result in results:
        bag_to_obj[bag].add_output(bag_to_obj[result[0]], int(result[1]))

for bag in bag_to_obj:
    bag_to_obj[bag].check_gold()

bag_to_obj["shiny gold"].contains_gold = False

print(sum(bag_to_obj[bag].contains_gold for bag in bag_to_obj))
print(bag_to_obj["shiny gold"].check_num_bags())

print(time.time()-start)

# from operator import itemgetter
#
# import networkx as nx
# import matplotlib.pyplot as plt
# graph = nx.Graph()
#
# for bag in bags:
#     results = bags[bag]
#     if results[0][0] == "other bags.":
#         continue
#
#     for result in results:
#         graph.add_edge(bag, result[0], weight=int(result[1]))

# # node_and_degree = graph.degree()
# # (largest_hub, degree) = sorted(node_and_degree, key=itemgetter(1))[-1]
# #
# # hub_ego = nx.ego_graph(graph, largest_hub)
# #
# # pos = nx.spring_layout(hub_ego)
# # nx.draw(hub_ego, pos, node_color="b", node_size=50, with_labels=True)
#
# options = {"node_size": 50, "with_labels": True, "node_color": "b", "cmap": plt.cm.Blues}
#
# # nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], **options)
# nx.draw(graph, **options)
# plt.show()