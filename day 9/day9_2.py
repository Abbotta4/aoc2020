with open('input.txt') as f:
    inputl = f.readlines()
    inputl = [int(x) for x in inputl]

def find_vuln(inputl):
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
                if queue[i] + queue[j] == queue[-1]:
                    valid = True
        if not valid:
            return queue[-1]

vuln_sum = find_vuln(inputl.copy())
for i in range(len(inputl)):
    for j in range(i + 2, len(inputl)):
        contig_sum = sum(inputl[i:j])
        if contig_sum == vuln_sum:
            contig_range = inputl[i:j].copy()
            contig_range.sort()
            print(contig_range[-1] + contig_range[0])
        elif contig_sum > vuln_sum:
            break
