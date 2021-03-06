import sys

data = sys.stdin.readlines()


front = 'F'
back = 'B'
left = 'L'
right = 'R'

highest_seat_id_list = []
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
    highest_seat_id_list.append(seat_id)

print(max(highest_seat_id_list))
