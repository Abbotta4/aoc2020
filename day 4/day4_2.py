import re

with open('input.txt') as f:
    inputl = f.read()

passports = inputl.split('\n\n')
valid_passports = 0
for passport in passports:
    byr = iyr = eyr = hgt = hcl = ecl = pid = False

    byr_r = re.search(r'byr:(\d{4})\b', passport)
    if byr_r != None:
        byr_d = int(byr_r.group(1))
        if byr_d >= 1920 and byr_d <= 2002:
            byr = True

    iyr_r = re.search(r'iyr:(\d{4})\b', passport)
    if iyr_r != None:
        iyr_d = int(iyr_r.group(1))
        if iyr_d >= 2010 and iyr_d <= 2020:
            iyr = True

    eyr_r = re.search(r'eyr:(\d{4})\b', passport)
    if eyr_r != None:
        eyr_d = int(eyr_r.group(1))
        if eyr_d >=2020 and eyr_d <= 2030:
            eyr = True

    hgt_r_cm = re.search(r'hgt:(\d+)cm\b', passport)
    if hgt_r_cm != None:
        hgt_d_cm = int(hgt_r_cm.group(1))
        if hgt_d_cm >= 150 and hgt_d_cm <= 193:
            hgt = True
    hgt_r_in = re.search(r'hgt:(\d+)in\b', passport)
    if hgt_r_in != None:
        hgt_d_in = int(hgt_r_in.group(1))
        if hgt_d_in >= 59 and hgt_d_in <= 76:
            hgt = True

    hcl = re.search(r'hcl:#([0-9a-f]{6})\b', passport) != None

    ecl_r = re.search(r'ecl:([a-z]{3}\b)', passport)
    if ecl_r != None:
        if ecl_r.group(1) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            ecl = True

    pid = re.search(r'pid:\d{9}\b', passport) != None

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid_passports += 1

print(valid_passports)
