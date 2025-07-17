import sys
input = sys.stdin.readline

N = int(input())
skyline = list(map(int, input().split()))
views = [[0] * N for _ in range(N)]

for b1 in range(N):
    h = skyline[b1]
    gradiant = -1000000000
    for b2 in range(b1+1, N):
        grad = (skyline[b2] - h) / (b2 - b1)
        if gradiant < grad:
            views[b1][b2] = 1
            views[b2][b1] = 1
            gradiant = grad

views_each = [0] * N
for i in range(N):
    for j in range(N):
        if views[i][j] == 1:
            views_each[i] += 1

views_each.sort()
print(views_each[-1])