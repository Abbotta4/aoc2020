with open('input.txt') as f:
    inputl = f.readlines()

memory = {}
while inputl:
    line = inputl.pop(0)
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
        continue
    mem, val = line.split(' = ')
    val = '{0:b}'.format(int(val)).zfill(36)
    masked_val = ''
    for mask_bit, val_bit in zip(mask, val):
        masked_val += val_bit if mask_bit == 'X' else mask_bit
    memory[mem] = int(masked_val, 2)

total = 0
for mem in memory:
    total += memory[mem]
print(total)
