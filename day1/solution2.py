import sys

data = [int(i) for i in sys.stdin.readlines()]
sums = 2020

for i,entry1 in enumerate(data):
    rest_of_data = data[i+1:]

    for entry2 in rest_of_data:
        if entry1 + entry2 >= sums:
            continue
        else:
            entry3 = sums - entry1 - entry2
            if entry3 > 0:
                search_data = rest_of_data[:]
                search_data.remove(entry2)
                if entry3 in search_data:
                    print(entry1*entry2*entry3)
                    break