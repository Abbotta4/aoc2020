from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

with open('input.txt') as f:
    timestamp = int(f.readline())
    buses = f.readline().strip().split(',')

inc = int(buses[0])
wait = inc
while True:
    found = True
    for bus in buses:
        if not found:
            break
        if bus == 'x':
            continue
        if (wait + buses.index(bus)) % int(bus) == 0:
            inc = lcm(inc, int(bus))
        else:
            found = False
            break
    if found:
        print(wait)
        break
    wait += inc
