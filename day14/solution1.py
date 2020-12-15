import sys

data = [ line.strip('\n') for line in sys.stdin.readlines() ]
skip = 'X'

mem_dict = {}
for line in data:
    if 'mask' in line:
        mask = line.split(' = ')[1]
    else:
        address = int(line.split(' = ')[0].split('[')[1][:-1])
        decimal = int(line.split(' = ')[1])
        str_bit = '{0:0' + str(len(mask)) + 'b}'
        value = str_bit.format(decimal)
    
        result = list(value)
        for i in range(len(mask)):
            v_pos = len(value) - 1 - i
            m_pos = len(mask) - 1 - i
            m_val = mask[m_pos]
            if m_val != skip:
                result[v_pos] = m_val

        bit_result = ''.join(result)
        int_result = int(bit_result,2)
        mem_dict[address] = int_result
        
print(sum(mem_dict.values()))