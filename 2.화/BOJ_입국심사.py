import sys
input = sys.stdin.readline
N, M = map(int, input().split())
immigration = [int(input()) for _ in range(N)]
immigration.sort()

start = 1
end = immigration[0] * M
ans = end

while(start <= end):
    mid = (start + end) // 2
    total = 0
    for i in immigration:
        total += mid // i
        if total >= M:
            break
    if total >= M:
        ans = mid
        end = mid -1
    if total < M:
        start = mid + 1

print(ans)    