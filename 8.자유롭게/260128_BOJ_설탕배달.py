import sys
input = sys.stdin.readline
N = int(input())
if N < 6:
    if N == 3 or N == 5:
        print(1)
    else:
        print(-1)
else:
    dp = [-1] * (N+1)
    dp[3], dp[5] = 1, 1
    for i in range(6, N+1):
        if dp[i-5] != -1:
            dp[i] = 1 + dp[i-5]
        elif dp[i-3] != -1:
            dp[i] = 1 + dp[i-3]
        else:
            dp[i] = -1
    print(dp[N])