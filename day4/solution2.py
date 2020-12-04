import sys

data = sys.stdin.readlines()
passports = []
requirements = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
ecl_req = ['amb','blu','brn','gry','grn','hzl','oth']

country_id = 'cid'
valid_passports = 0

new_passport = {}
for line in data:
    if '\n' == line:
        passports.append(new_passport)
        new_passport = {}
    else:
        line = line[:-1]
        for i in line.split(' '):
            key = i.split(':')[0]
            value = i.split(':')[1]

            if key != country_id:
                new_passport[key] = value

for passport in passports:
    if set(requirements) - set(passport) == set():
        if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            continue
        if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            continue
        if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            continue
        if len(passport['pid']) != 9:
            continue
        try:
            int(passport['pid'])
        except ValueError:
            continue
        if passport['ecl'] not in ecl_req:
            continue
        if passport['hcl'][0] != '#' or len(passport['hcl'][1:]) != 6:
            continue
        if 'cm' in passport['hgt']:
            if int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
                continue
        elif 'in' in passport['hgt']:
            if int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76:
                continue
        else:
            continue
        valid_passports += 1

print(valid_passports)