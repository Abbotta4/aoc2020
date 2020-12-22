with open('input.txt') as f:
    inputl = f.readlines()

def check_seat(row, col):
    seats = distance = 0
    n = ne = e = se = s = sw = w = nw = False
    while distance < max(len(inputl), len(inputl[0])):
        distance += 1
        if not n:
            if row - distance < 0:
                n = True
            else:
                seat = inputl[row - distance][col]
                if seat in ('L', '#'):
                    n = True
                if seat == '#':
                    seats += 1
        if not ne:
            if row - distance < 0 or col + distance >= len(inputl[0]):
                ne = True
            else:
                seat = inputl[row - distance][col + distance]
                if seat in ('L', '#'):
                    ne = True
                if seat == '#':
                    seats += 1
        if not e:
            if col + distance >= len(inputl[0]):
                e = True
            else:
                seat = inputl[row][col + distance]
                if seat in ('L', '#'):
                    e = True
                if seat == '#':
                    seats += 1
        if not se:
            if row + distance >= len(inputl) or col + distance >= len(inputl[0]):
                se = True
            else:
                seat = inputl[row + distance][col + distance]
                if seat in ('L', '#'):
                    se = True
                if seat == '#':
                    seats += 1
        if not s:
            if row + distance >= len(inputl):
                s = True
            else:
                seat = inputl[row + distance][col]
                if seat in ('L', '#'):
                    s = True
                if seat == '#':
                    seats += 1
        if not sw:
            if row + distance >= len(inputl) or col - distance < 0:
                sw = True
            else:
                seat = inputl[row + distance][col - distance]
                if seat in ('L', '#'):
                    sw = True
                if seat == '#':
                    seats += 1
        if not w:
            if col - distance < 0:
                w = True
            else:
                seat = inputl[row][col - distance]
                if seat in ('L', '#'):
                    w = True
                if seat == '#':
                    seats += 1
        if not nw:
            if row - distance < 0 or col - distance < 0:
                nw = True
            else:
                seat = inputl[row - distance][col - distance]
                if seat in ('L', '#'):
                    nw = True
                if seat == '#':
                    seats += 1
        if n and ne and e and se and s and sw and w and nw:
            break
    return seats

def _check_seat(row, col):
    seats = distance = 0
    n = ne = e = se = s = sw = w = nw = False
    _seats = ''
    while distance < max(len(inputl), len(inputl[0])):
        distance += 1
        if not n:
            if row - distance < 0:
                n = True
            else:
                seat = inputl[row - distance][col]
                if seat in ('L', '#'):
                    n = True
                if seat == '#':
                    _seats += ' n'
                    seats += 1
        if not ne:
            if row - distance < 0 or col + distance >= len(inputl[0]):
                ne = True
            else:
                seat = inputl[row - distance][col + distance]
                if seat in ('L', '#'):
                    ne = True
                if seat == '#':
                    _seats += ' ne'
                    seats += 1
        if not e:
            if col + distance >= len(inputl[0]):
                e = True
            else:
                seat = inputl[row][col + distance]
                if seat in ('L', '#'):
                    e = True
                if seat == '#':
                    _seats += ' e'
                    seats += 1
        if not se:
            if row + distance >= len(inputl) or col + distance >= len(inputl[0]):
                se = True
            else:
                seat = inputl[row + distance][col + distance]
                if seat in ('L', '#'):
                    se = True
                if seat == '#':
                    _seats += ' se'
                    seats += 1
        if not s:
            if row + distance >= len(inputl):
                s = True
            else:
                seat = inputl[row + distance][col]
                if seat in ('L', '#'):
                    s = True
                if seat == '#':
                    _seats += ' s'
                    seats += 1
        if not sw:
            if row + distance >= len(inputl) or col - distance < 0:
                sw = True
            else:
                seat = inputl[row + distance][col - distance]
                if seat in ('L', '#'):
                    sw = True
                if seat == '#':
                    _seats += ' sw'
                    seats += 1
        if not w:
            if col - distance < 0:
                w = True
            else:
                seat = inputl[row][col - distance]
                if seat in ('L', '#'):
                    w = True
                if seat == '#':
                    _seats += ' w'
                    seats += 1
        if not nw:
            if row - distance < 0 or col - distance < 0:
                nw = True
            else:
                seat = inputl[row - distance][col - distance]
                if seat in ('L', '#'):
                    nw = True
                if seat == '#':
                    _seats += ' nw'
                    seats += 1
        if n and ne and e and se and s and sw and w and nw:
            break
    print(_seats)
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
                if num_seats >= 5:
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
print(_check_seat(0, 2))
inputl, changed = musical_seats(inputl)
#print(inputl)
print_seats()
'''
