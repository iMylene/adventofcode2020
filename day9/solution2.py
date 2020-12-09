import sys

data = [ int(i) for i in sys.stdin.readlines() ]
preamble_length = 25
preamble = data[:preamble_length]
rest_data = data[preamble_length:]

for number in rest_data:
    #check if it's a summer of the preamble
    found = False
    for cnt, prev_num1 in enumerate(preamble):
        if found:
            break
        #make sums with the prev_num1 and the rest of the preamble
        for prev_num2 in preamble[cnt+1:]:
            summer = prev_num1 + prev_num2
            
            #invalid number
            if summer == number:
                found = True
                break
    if not found:
        invalid_number = number
        print(number)
        break

    preamble = preamble[1:]+[number]

for i in range(len(data)):
    for j in range(i+1,1+len(data)):
        new_data = data[i:j]
        new_sum = sum(new_data)
        if invalid_number == new_sum:
            minimum = min(new_data)
            maximum = max(new_data)
            print(minimum+maximum)
            exit()
