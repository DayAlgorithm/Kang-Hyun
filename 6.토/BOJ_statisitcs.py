from decimal import *
N = int(input())
integers = [int(input()) for _ in range(N)]
integers = sorted(integers)

sum = 0
for i in integers:
    sum += i

avg = sum / N
decimal_avg = Decimal(str(avg))
rounded_avg = decimal_avg.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
if rounded_avg == Decimal("-0"):
    print("0")
else:
    print(rounded_avg)

median = integers[N//2]
print(median)

mode = [integers[0]]
max_freq = 0
cur_freq = 1
for i in range(1, N):
    if integers[i] == integers[i-1]:
        cur_freq += 1
    else:
        cur_freq = 1
    if cur_freq > max_freq:
        max_freq = cur_freq
        mode = []
        mode.append(integers[i])
    elif cur_freq == max_freq:
        mode.append(integers[i])
mode = sorted(mode)
if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])
    
integers_range = integers[-1] - integers[0]
print(integers_range)