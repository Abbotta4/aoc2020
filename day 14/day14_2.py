with open('input.txt') as f:
    inputl = f.readlines()

memory = {}
while inputl:
    line = inputl.pop(0)
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
        continue
    mem, val = line.split(' = ')
    mem = '{0:b}'.format(int(mem[4:-1])).zfill(36)
    addresses = ['']
    for mask_bit, mem_bit in zip(mask, mem):
        _addresses = []
        for address in addresses:
            if mask_bit == '0':
                _addresses.append(address + mem_bit)
            elif mask_bit == '1':
                _addresses.append(address + '1')
            else: # == 'X'
                _addresses.append(address + '0')
                _addresses.append(address + '1')
        addresses = _addresses
    for address in addresses:
        memory[address] = int(val)

total = 0
for mem in memory:
    total += memory[mem]
print(total)
