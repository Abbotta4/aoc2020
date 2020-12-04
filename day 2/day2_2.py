import re

with open('input.txt') as f:
    inputl = f.readlines()
    
valid_passwords = 0
for entry in inputl:
    regex = re.search("(\d+)-(\d+) (.): (.*)", entry)
    index1 = int(regex.group(1)) - 1
    index2 = int(regex.group(2)) - 1
    letter = regex.group(3)
    password = regex.group(4)
    if index1 >= len(password) or index2 >= len(password):
        continue
    if (password[index1] == letter or password[index2] == letter) and password[index1] != password[index2]:
        valid_passwords += 1

print(valid_passwords)
