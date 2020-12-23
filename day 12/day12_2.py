with open('input.txt') as f:
    inputl = f.readlines()

directions = ['N', 'E', 'S', 'W']
direction = 1 # east
sew = sns = 0
wew, wns = 10, 1
for instruction in inputl:
    inst, length = instruction[0], int(instruction[1:])
    if inst == 'F':
        for move in range(length):
            sew += wew
            sns += wns
    if inst == 'N':
        wns += length
    elif inst == 'E':
        wew += length
    elif inst == 'S':
        wns -= length
    elif inst == 'W':
        wew -= length
    elif inst in ('L', 'R'):
        length %= 360
        if inst == 'L':
            length = 360 - length # convert L to R
        if length == 90:
            wew, wns = wns, -wew
        elif length == 180:
            wew, wns = -wew, -wns
        elif length == 270:
            wew, wns = -wns, wew
print(abs(sew) + abs(sns))
