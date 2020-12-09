with open('input.txt') as f:
    instructions = f.readlines()

def run(instructions):
    pc = 0
    accumulator = 0
    visited = []
    while pc < len(instructions):
        if pc in visited:
            return False
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
    return True

for pc in range(len(instructions)):
    inst, arg = instructions[pc].split(' ')
    #print('inst: {0}\narg: {1}\npc: {2}\n'.format(inst, arg.strip(), pc))
    if inst == 'jmp':
        _instructions = instructions.copy()
        _instructions[pc] = 'nop ' + arg
        if run(_instructions):
            break
    elif inst == 'nop':
        _instructions = instructions.copy()
        _instructions[pc] = 'jmp ' + arg
        if run(_instructions):
            break
