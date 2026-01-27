import sys
input = sys.stdin.readline

n = int(input())
step = [0] * (n + 1)
for i in range(1, n + 1):
    step[i] = int(input())

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = step[1]
if n >= 2:
    dp[2] = step[1] + step[2]
if n >= 3:
    for i in range(3, n + 1):
        dp[i] = max(dp[i-2] + step[i], dp[i-3] + step[i-1] + step[i])

print(dp[n])