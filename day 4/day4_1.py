import re

with open('input.txt') as f:
    inputl = f.read()

passports = inputl.split('\n\n')
valid_passports = 0
for passport in passports:
    byr = re.search("byr:", passport) != None
    iyr = re.search("iyr:", passport) != None
    eyr = re.search("eyr:", passport) != None
    hgt = re.search("hgt:", passport) != None
    hcl = re.search("hcl:", passport) != None
    ecl = re.search("ecl:", passport) != None
    pid = re.search("pid:", passport) != None
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid_passports += 1

print(valid_passports)
