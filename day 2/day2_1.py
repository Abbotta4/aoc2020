import re

with open('input.txt') as f:
    inputl = f.readlines()
    
valid_passwords = 0
for entry in inputl:
    regex = re.search("(\d+)-(\d+) (.): (.*)", entry)
    min = int(regex.group(1))
    max = int(regex.group(2))
    letter = regex.group(3)
    password = regex.group(4)
    letter_freq = len(re.findall(letter, password))
    if letter_freq <= max and letter_freq >= min:
        valid_passwords += 1

print(valid_passwords)
