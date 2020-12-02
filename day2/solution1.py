import sys

data = sys.stdin.readlines()
lines = [ i.split(':') for i in data ]
valid = 0

for line in lines:
    policy = line[0]
    password = line[1].replace(" ", "")
    
    read_policy = policy.split('-')
    mininum = int(read_policy[0])
    maximum = int(read_policy[1].split()[0])
    letter = read_policy[1].split()[1]
    
    count_letters = password.count(letter)
    if count_letters <= maximum and count_letters >= mininum:
        valid +=1

print(valid)