import sys
input = sys.stdin.readline
N, M = map(int, input().split())
days = [int(input()) for _ in range(N)]

low = max(days)
high = max(days) * N
ans = high

while(low <= high):
    mid = (low + high) // 2
    withdraws = 0
    left = 0
    for d in days:
        if left < d:
            withdraws += 1
            left = mid - d
        else:
            left -= d
    if withdraws > M:
        low = mid + 1
    else:
        ans = mid
        high = mid - 1
print(ans)