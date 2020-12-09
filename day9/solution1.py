import sys

data = [ int(i) for i in sys.stdin.readlines() ]
preamble_length = 25
preamble = data[:preamble_length]
rest_data = data[preamble_length:]

for number in rest_data:
    #check if it's a sum of the preamble
    found = False
    for cnt, prev_num1 in enumerate(preamble):
        if found:
            break
        #make sums with the prev_num1 and the rest of the preamble
        for prev_num2 in preamble[cnt+1:]:
            sum = prev_num1 + prev_num2
            
            #invalid number
            if sum == number:
                found = True
                break
    if not found:
        print(number)
        break

    preamble = preamble[1:]+[number]