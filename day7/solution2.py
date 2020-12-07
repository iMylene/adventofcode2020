import sys

data = sys.stdin.readlines()
shiny = 'shiny gold'
bags = 0

rules = dict()
for line in data:
    key = " ".join(line.split()[0:2])
    values = []
    if 'no other' not in line:
        i = 4
        j = 7
        string = " ".join(line.split()[i:j])
        values.append(string)

        while len(line.split()) > j + 1:
            i+= 4
            j+= 4
            string = " ".join(line.split()[i:j])
            values.append(string)
    rules[key] = values

search_list = [(rules[shiny],1)]
visited = []

while search_list != []:
    new_search_list = []
    for rule,cnt in search_list:
        for cbag in rule:
            number = int(cbag.split()[0])
            bags += number*cnt
            search_item = ' '.join(cbag.split()[1:])
            new_search_list.append((rules[search_item],number*cnt))
    search_list = new_search_list[:]
print(bags)