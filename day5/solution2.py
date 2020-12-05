import sys

data = sys.stdin.readlines()


front = 'F'
back = 'B'
left = 'L'
right = 'R'

seat_id_list = []
for ticket in data:
    row_seats_max = 127
    row_seats_min = 0
    col_seats_max = 7
    col_seats_min = 0
    seat_id = 0
    
    for char in ticket:
        if char == front:
            row_seats_max = (row_seats_min+row_seats_max)//2
        elif char == back:
            row_seats_min = 1 + (row_seats_min+row_seats_max)//2
        elif char == left:
            col_seats_max = (col_seats_min+col_seats_max)//2
        elif char == right:
            col_seats_min = 1 + (col_seats_min+col_seats_max)//2

    seat_id = row_seats_max * 8 + col_seats_max
    seat_id_list.append(seat_id)

for seat_id in sorted(seat_id_list):
    if seat_id + 2 in seat_id_list and seat_id + 1 not in seat_id_list:
        print(seat_id+1)
