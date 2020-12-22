with open('input1.txt') as f:
    inputl = f.readlines()

def check_seat(row, col):
    seats = 0
    for rmod in +1, 0, -1:
        for cmod in +1, 0, -1:
            if row + rmod < 0 or col + cmod < 0:
                continue
            if row + rmod >= len(inputl) or col + cmod >= len(inputl[0]):
                continue
            if rmod == cmod == 0:
                continue
            if inputl[row+rmod][col+cmod] == '#':
                    seats += 1
    return seats

def musical_seats(seats):
    new_seats = []
    changed = False
    for row in range(len(seats)):
        new_seats.append([])
        for col in range(len(seats[0])):
            seat = seats[row][col]
            num_seats = check_seat(row, col)
            if seat == '.':
                new_seats[row] += '.'
            elif seat == 'L':
                if num_seats == 0:
                    new_seats[row] += '#'
                    changed = True
                else:
                    new_seats[row] += 'L'
            elif seat == '#':
                if num_seats >= 4:
                    new_seats[row] += 'L'
                    changed = True
                else:
                    new_seats[row] += '#'
    return (new_seats, changed)

while True:
    inputl, changed = musical_seats(inputl)
    if not changed:
        break

occupied = 0
for row in inputl:
    for col in row:
        if col == '#':
            occupied += 1
print(occupied)
'''
def print_seats():
    for row in inputl:
        for col in row:
            print(col.strip(), end='')
        print('')


inputl, changed = musical_seats(inputl)
inputl, changed = musical_seats(inputl)
#print(inputl)
print_seats()
'''
