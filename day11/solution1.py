import sys

data = [ line.strip('\n') for line in sys.stdin.readlines() ]
maxrow = len(data)
maxcol = len(data[0])
maxocc = 4

#first round, fill all the empty seats with persons:
occ = [ line.replace('L','#') for line in data ]

#make dict with the occupied seat as key and the num of neigh as value
neigh_dict = {}
for i, row in enumerate(occ):
    for j, col in enumerate(occ):
        if '#' in occ[i][j]:
            #count num of neigh
            counter = 0

            #check: up, diag upperleft, diag upperright
            if i != 0:
                if '#' in occ[i-1][j]:
                    counter += 1
                if j != 0 and '#' in occ[i-1][j-1]:
                    counter += 1
                if j != maxcol - 1 and '#' in occ[i-1][j+1]:
                    counter += 1

            #check: same level neigh: left and right
            if j != 0 and '#' in occ[i][j-1]:
                    counter += 1
            if j != maxcol - 1 and '#' in occ[i][j+1]:
                    counter += 1
            
            #check: down, diag lowerleft, diag lowerright
            if i != maxrow - 1:
                if '#' in occ[i+1][j]:
                    counter += 1
                if j != 0 and '#' in occ[i+1][j-1]:
                    counter += 1
                if j != maxcol - 1 and '#' in occ[i+1][j+1]:
                    counter += 1

            neigh_dict[i,j] = counter
            if neigh_dict[i,j] >= maxocc:
                del neigh_dict[i,j]
print(neigh_dict) 
