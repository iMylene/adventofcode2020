import sys

data = sys.stdin.readlines()
shiny = 'shiny gold'

inverted = dict()
for line in data:
    key = " ".join(line.split()[0:2])
    values = []
    if 'no other' not in line:
        i = 5
        j = 7
        string = " ".join(line.split()[i:j])
        values.append(string)

        while len(line.split()) > j + 1:
            i+= 4
            j+= 4
            string = " ".join(line.split()[i:j])
            values.append(string)

        for val in values:
            if val not in inverted.keys():
                inverted[val] = []
            inverted[val].append(key)

count_colors = inverted[shiny]
search_list = inverted[shiny]
visited = []
visited.append(shiny)
while search_list != []:
    new_search_list = []
    for i in search_list:
        visited.append(i)

        if i not in inverted.keys():
            continue
        count_colors += inverted[i]
        for j in inverted[i]:
            if j not in visited:
                new_search_list += inverted[i]
    search_list = list(set(new_search_list))

print(len(set(count_colors)))
    