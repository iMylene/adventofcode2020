import sys

data = [int(i) for i in sys.stdin.readlines()]
sums = 2020

for i,entry1 in enumerate(data):
    rest_of_data = data[i+1:len(data)]
    entry2 = sums - entry1
    if entry2 in rest_of_data:
        break

print(entry1*entry2)