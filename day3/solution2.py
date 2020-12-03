import sys

data = sys.stdin.readlines()
slope_list = [(1,1),(1,3),(1,5),(1,7),(2,1)]

trees_list = []
max_r = len(data) - 1
max_c = len(data[0]) - 2

for i,slope in enumerate(slope_list):
    trees = 0
    r_slope = slope[0]
    c_slope = slope[1]

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
    trees_list.append(trees)

result = 1
for x in trees_list:
    result = result * x 
print(result)