import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
idx = N-1
req = 0
while(K > 0 and idx >= 0):
    if coins[idx] > K:
        idx -= 1
    elif coins[idx] == K:
       req += 1
       break
    else:
        req += K // coins[idx]
        K -= (K // coins[idx]) * coins[idx]
        idx -= 1
print(req)