import sys

data = sys.stdin.readlines()
passports = []
requirements = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
country_id = 'cid'
valid_passports = 0

new_passport = []
for line in data:
    if '\n' == line:
        if country_id in new_passport:
            new_passport.remove(country_id)
        passports.append(new_passport)
        new_passport = []
    else:
        [ new_passport.append(i.split(':')[0]) for i in line.split(' ') ]

for passport in passports:
    if set(requirements) - set(passport) == set():
        valid_passports += 1

print(valid_passports)