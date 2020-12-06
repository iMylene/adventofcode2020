import sys

data = sys.stdin.readlines()

group = dict()
size_group = 0
sums = 0
for line in data:
    if '\n' == line:
        for letter in group:
            if group[letter] == size_group:
                sums += 1
        
        group = dict()
        size_group = 0
    else:
        size_group += 1
        for char in line:
            if char == '\n':
                continue
            elif char not in group.keys():
                group[char] = 1
            else:
                group[char] = group[char] + 1

print(sums)