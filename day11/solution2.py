import sys

data = [ list(line.strip('\n')) for line in sys.stdin.readlines() ]
maxrow = len(data)
maxcol = len(data[0])
maxocc = 5
change = True

mutations = [(x,y) for x in [-1,0,1] for y in [-1,0,1]]
mutations.remove((0,0))

def valid(x,y):
    if x < 0 or y < 0:
        return False
    if x >= maxcol or y >= maxrow:
        return False
    return True

while change:
    change = False
    temp_data = []
    for y,r in enumerate(data):
        temp_row = []
        for x,s in enumerate(r):
            if s == '.':
                temp_row.append('.')
                continue
            if s == 'L':
                occ = 0
                for mutation in mutations:
                    if occ>0:
                        continue
                    dx, dy = mutation
                    nx, ny = x+dx, y+dy
                    if valid(nx,ny) and data[ny][nx] == '#':
                        occ += 1
                if occ==0:
                    temp_row.append('#')
                    change = True
                else:
                    temp_row.append('L')
            if s == '#':
                occ = 0
                for mutation in mutations:
                    if occ>=maxocc:
                        continue
                    dx, dy = mutation
                    nx, ny = x+dx, y+dy
                    if valid(nx,ny) and data[ny][nx] == '#':
                        occ += 1
                if occ>=maxocc:
                    temp_row.append('L')
                    change = True
                else:
                    temp_row.append('#')
        temp_data.append(temp_row[:])   
    data = temp_data[:]

occ = 0
for r in data:
    for s in r:
        if s == '#':
            occ += 1
print(occ)