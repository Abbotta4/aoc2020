with open('input.txt') as f:
    inputl = f.readlines()

width = len(inputl[0]) - 1
position = 0
trees = 0

while True:
    inputl.pop(0)
    if not inputl:
        break
    position += 3
    square = inputl[0][position % width]
    if square == '#':
        trees += 1

print(trees)
