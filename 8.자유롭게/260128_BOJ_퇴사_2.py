import sys
input = sys.stdin.readline
N = int(input())

dp = [0] * (N+1)

task_over = [[] for _ in range(N+1)]
for i in range(1, N+1):
    T, P = map(int, input().split())
    if i + T - 1 <= N: 
        task_over[i + T - 1].append((i, P)) # start day and price

for i in range(1, N+1):
    if len(task_over[i]) == 0:
        dp[i] = dp[i-1]
    else:
        best_case = dp[i-1]
        for item in task_over[i]:
            value = item[1] + dp[item[0]-1]
            best_case = max(best_case, value)
        dp[i] = best_case

print(dp[N])    