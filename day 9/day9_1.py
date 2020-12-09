with open('input.txt') as f:
    inputl = f.readlines()

queue = []
for preamble in range(25):
    queue.append(inputl.pop(0))
while inputl:
    queue.append(inputl.pop(0))
    valid = False
    for i in range(-26, -1):
        if valid:
            break
        for j in range(i + 1, -1):
            if valid:
                break
            if int(queue[i]) + int(queue[j]) == int(queue[-1]):
                valid = True
    if not valid:
        print(queue[-1].strip())
        inputl = False
