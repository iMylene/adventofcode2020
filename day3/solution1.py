import sys

data = sys.stdin.readlines()
trees = 0
r = 1
c = 3
max_r = len(data) - 1
max_c = len(data[0]) - 2

while True:
    if data[r][c] == '#':
        trees += 1

    r+= 1
    if r > max_r:
        break

    c+= 3
    if c > max_c:
        c = c - max_c - 1

print(trees)