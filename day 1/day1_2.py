with open('input.txt') as f:
    inputl = f.readlines()

for i in range(len(inputl)):
    for j in range(i + 1, len(inputl)):
        for k in range(j + 1, len(inputl)):
            sum = int(inputl[i]) + int(inputl[j]) + int(inputl[k])
            if sum == 2020:
                print(int(inputl[i]) * int(inputl[j]) * int(inputl[k]))
                exit(0)
print("didn't find");
exit(1)
