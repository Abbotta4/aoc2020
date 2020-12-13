with open('input.txt') as f:
    inputl = f.readlines()

inputl = sorted([int(x) for x in inputl])
last = j1 = j3 = 0
for adapter in inputl:
    if adapter - last == 1:
        j1 += 1
    elif adapter - last == 3:
        j3 += 1
    elif adapter - last > 3:
        break
    last = adapter
print(j1 * (j3 + 1))
