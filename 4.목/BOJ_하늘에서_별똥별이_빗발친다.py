import sys
input = sys.stdin.readline
N, M, L, K = map(int, input().split())
xs = []
ys = []
asteroids = []
for _ in range(K):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    asteroids.append((x,y))

max_blocked = 0

for x in xs:
    for y in ys:
        blocked = 0
        right = x + L 
        up = y + L 
        if right > N:
            x -= (right - N)
            right -= (right - N)
        if up > M:
            y -= (up - M)
            up -= (up - M)
        for a in asteroids:
            if x <= a[0] and a[0] <= right and y <= a[1] and a[1] <= up:
                blocked += 1
        if max_blocked < blocked:
            max_blocked = blocked

print(K - max_blocked)