import sys

data = [ line.split() for line in sys.stdin.readlines() ]

def run_instruct(data):
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
            return

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
            print(acc)
            return

for ind,chnk in enumerate(data):
    if chnk[0] == 'acc':
        continue
    if chnk[0] == 'nop':
        newdata = data[:ind] + [('jmp',chnk[1])] + data[ind+1:]
    if chnk[0] == 'jmp':
        newdata = data[:ind] + [('nop',chnk[1])] + data[ind+1:]
    run_instruct(newdata)