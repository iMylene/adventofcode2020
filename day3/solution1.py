import sys

data = sys.stdin.readlines()
trees = 0
r_slope = 1
c_slope = 3

max_r = len(data) - 1
max_c = len(data[0]) - 2

r = r_slope
c = c_slope
while True:
    if data[r][c] == '#':
        trees += 1

    r+= r_slope
    if r > max_r:
        break

    c+= c_slope
    if c > max_c:
        c = c - max_c - 1

print(trees)