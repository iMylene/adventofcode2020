import sys

data = [ int(i) for i in sys.stdin.readlines() ]
data = sorted(data)

arrangements = []
arrangements.append(data)
first = arrangements[0][0]
last = arrangements[0][-1]

#build the smallest arrangement
prev = first
smallest_arr = [first] + [last]
building_arr = True
while building_arr:
    if prev + 3 == last or prev + 2 == last or prev + 1 == last:
        building_arr = False
    elif prev + 3 in data:
        smallest_arr.append(prev + 3)
        prev = prev + 3
    elif prev + 2 in data:
        smallest_arr.append(prev + 2)
        prev = prev + 2
    elif prev + 1 in data:
        smallest_arr.append(prev + 1)
        prev = prev + 1
arrangements.append(sorted(smallest_arr))

#build the rest of the arr

print(arrangements)