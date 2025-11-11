import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

shortest = 1
longest = max(lans)
ans = longest

while(shortest <= longest):
    mid = (shortest + longest) // 2
    total = 0
    for l in lans:
        total += l // mid
        if total >= N:
            break
    if total >= N:
        ans = mid
        shortest = mid + 1
    else:
        longest = mid -1
print(ans)        