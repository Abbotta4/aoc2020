with open('input.txt') as f:
    inputl = f.readlines()
inputl = sorted([int(x) for x in inputl])
inputl.insert(0, 0)

def calc_ways(adapters):
    cache = {}

    def _calc_ways(adapters):
        if str(adapters) in cache:
            return cache[str(adapters)]
        
        sum = 0
        for adapter in adapters[-4:-1]:
            if adapters[-1] - adapter <= 3:
                index = adapters.index(adapter) + 1
                sum += _calc_ways(adapters[:index])
        cache[str(adapters)] = sum or 1
        return sum or 1

    return _calc_ways(adapters)

print(calc_ways(inputl))
