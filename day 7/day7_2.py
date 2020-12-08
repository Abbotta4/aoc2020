with open('input.txt') as f:
    inputl = f.readlines()

contains = {}
is_contained_by = {}
for rules in inputl:
    root, leaves = rules[:-2].split('s contain ')
    root = ' '.join(root.split(' ')[:-1])
    leaves = leaves.split(', ')
    leaves = [[leaf.split(' ')[0], ' '.join(leaf.split(' ')[1:-1])] for leaf in leaves]
    contains[root] = leaves
    for leaf in leaves:
        if leaf[1] in is_contained_by.keys():
            is_contained_by[leaf[1]].append(root)
        else:
            is_contained_by[leaf[1]] = [root]

bags = []
for bag in contains['shiny gold']:
    for quantity in range(int(bag[0])):
        bags.append(bag[1])
for bag in bags:
    for bag_bag in contains[bag]:
        if bag_bag[0] != 'no':
            for x in range(int(bag_bag[0])):
                bags.append(bag_bag[1])
print(len(bags))
