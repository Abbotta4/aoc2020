with open('input.txt') as f:
    inputl = f.readlines()

seats = []
for bsp in inputl:
    row = int(bsp[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(bsp[7:].replace('L', '0').replace('R', '1'), 2)
    seats.append(row * 8 + col)
seats.sort()

while len(seats) > 1:
    if seats[1] and seats[1] != seats[0] + 1:
        print(seats[0] + 1)
        break
    seats.pop(0)
