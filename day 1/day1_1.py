with open('input.txt') as f:
    inputl = f.readlines()

for i in range(len(inputl)):
    for j in range(i + 1, len(inputl)):
        sum = int(inputl[i]) + int(inputl[j])
        if sum == 2020:
            print(int(inputl[i]) * int(inputl[j]))
            exit(0)
print("didn't find");
exit(1)
