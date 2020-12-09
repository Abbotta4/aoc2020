with open('input.txt') as f:
    instructions = f.readlines()

pc = 0
accumulator = 0
visited = []
while True:
    if pc in visited:
        break
    visited.append(pc)
    inst, arg = instructions[pc].split(' ')
    if inst == 'acc':
        accumulator += int(arg)
        pc += 1
    elif inst == 'jmp':
        pc += int(arg)
    else: # nop
        pc += 1
print(accumulator)
