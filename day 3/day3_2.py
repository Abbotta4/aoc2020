with open('input.txt') as f:
    inputl = f.readlines()

width = len(inputl[0]) - 1

def calc_trees(right, down):
    slope = inputl.copy()
    position = 0
    trees = 0
    
    while True:
        for i in range(down):
            if slope:
                slope.pop(0)
        if not slope:
            break
        position += right
        square = slope[0][position % width]
        if square == '#':
            trees += 1
    return trees

print(calc_trees(1, 1) * calc_trees(3, 1) * calc_trees(5, 1) * calc_trees(7, 1) * calc_trees(1, 2))
