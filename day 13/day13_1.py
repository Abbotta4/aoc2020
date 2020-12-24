with open('input.txt') as f:
    timestamp = int(f.readline())
    buses = f.readline().strip().split(',')

buses = [int(x) for x in buses if x != 'x']
wait = 0
found = False
while True:
    time = timestamp + wait
    for bus in buses:
        if time % bus == 0:
            found = True
            print(bus * wait)
            break
    if found:
        break
    wait += 1
