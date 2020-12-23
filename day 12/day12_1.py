with open('input.txt') as f:
    inputl = f.readlines()

directions = ['N', 'E', 'S', 'W']
direction = 1 # east
ew = ns = 0
for instruction in inputl:
    inst, length = instruction[0], int(instruction[1:])
    if inst == 'F':
        inst = directions[direction]
    if inst == 'N':
        ns += length
    elif inst == 'E':
        ew += length
    elif inst == 'S':
        ns -= length
    elif inst == 'W':
        ew -= length
    elif inst == 'L':
        length //= 90
        direction = (direction - length) % 4
    elif inst == 'R':
        length //= 90
        direction = (direction + length) % 4
print(abs(ew) + abs(ns))
