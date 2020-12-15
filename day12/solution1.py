import sys

data = [ line.strip('\n') for line in sys.stdin.readlines() ]
facing = 'E'
actions = ['N', 'S', 'E', 'W', 'F', 'L', 'R'] 

change_facing = ['L', 'R']
degrees = [0, 90, 180, 270, 360]

for instruct in data:
    letter = instruct[0]
    value = instruct[1:]

    if letter in change_facing:
