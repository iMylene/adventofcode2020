import sys

data = [ int(i) for i in sys.stdin.readlines() ]
data = sorted(data)

diff = 0
prev = 0

diff_1 = 1
diff_3 = 3

cnt_diff_1 = 0
cnt_diff_3 = 1

for num in data:
    diff = num - prev
    prev = num

    if diff == diff_1:
        cnt_diff_1 += 1
    elif diff == diff_3:
        cnt_diff_3 += 1

print(cnt_diff_1*cnt_diff_3)