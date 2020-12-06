import sys

data = sys.stdin.readlines()
groups = []

new_group = set()
for line in data:
    if '\n' == line:
        new_group.remove('\n')
        groups.append(new_group)
        new_group = set()
    else:
        for char in line:
            new_group.add(char)

sums = 0
for group in groups:
    sums += len(group)
print(sums)