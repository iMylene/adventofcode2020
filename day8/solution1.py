import sys

data = [ line.split() for line in sys.stdin.readlines() ]
acc = 0
visited_indices = []

i = 0
while True:
    #Read data
    instruction = data[i]
    op = instruction[0]

    #Save indices, check visited indices
    if i not in visited_indices:
        visited_indices.append(i)
    else:
        break 

    #Follow instruction
    if op == 'nop':
        i += 1
    else:
        arg = int(instruction[1])

        if op == 'acc':
            i += 1
            acc += arg
        else: #op == 'jmp'
            i += arg

    #Check if next i is in range
    if i >= len(data):
        break

print(acc)    