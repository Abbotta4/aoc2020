with open('input.txt') as f:
    inputl = f.readlines()

contains = {}
is_contained_by = {}
for rules in inputl:
    root, leaves = rules[:-2].split('s contain ')
    root = ' '.join(root.split(' ')[:-1])
    leaves = leaves.split(', ')
    leaves = [' '.join(leaf.split(' ')[1:-1]) for leaf in leaves]
    contains[root] = leaves
    for leaf in leaves:
        if leaf in is_contained_by.keys():
            is_contained_by[leaf].append(root)
        else:
            is_contained_by[leaf] = [root]

bags = []
containers = is_contained_by['shiny gold']
for bag in containers:
    bags.append(bag)
    if bag in is_contained_by.keys():
        for container_bag in is_contained_by[bag]:
            if container_bag not in containers:
                containers.append(container_bag)
print(len(bags))
