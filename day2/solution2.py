import sys

data = sys.stdin.readlines()
lines = [ i.split(':') for i in data ]
valid = 0

for line in lines:
    policy = line[0]
    password = line[1].replace(" ", "")

    read_policy = policy.split('-')
    position_1 = int(read_policy[0]) - 1
    position_2 = int(read_policy[1].split()[0]) - 1
    letter = read_policy[1].split()[1]

    if password[position_1] == letter and password[position_2] != letter:
        valid +=1
    if password[position_1] != letter and password[position_2] == letter:
        valid +=1

print(valid)