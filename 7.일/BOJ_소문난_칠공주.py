import sys
input = sys.stdin.readline
classroom = [list(input().strip()) for _ in range(5)]

directions = [(1,0), (0,1), (-1, 0), (0, -1)]

def dp(girls_needed, trace, ss):
    if girls_needed == 0:
        if ss >= 4:
            vis[trace[-1][0]][trace[-1][1]] = 0
            return 1
        else:
            vis[trace[-1][0]][trace[-1][1]] = 0
            return 0
    ways = 0
    for t in trace:
        for d in directions:
            ny, nx = t[0] + d[0], t[1] + d[1]
            if ny < 0 or nx < 0 or ny > 4 or nx > 4:
                continue
            if vis[ny][nx] == 0 and classroom[ny][nx] != 'A':
                vis[ny][nx] = 1
                if classroom[ny][nx] == 'S':
                    print("click " + str(girls_needed))
                    trace.append((ny,nx))
                    ways += dp(girls_needed-1, trace, ss+1)
                    vis[ny][nx] = 0
                else:
                    print("clock " + str(girls_needed))
                    trace.append((ny,nx))
                    ways += dp(girls_needed-1, trace, ss)
                    vis[ny][nx] = 0                
    return ways

howmany_s = 0
for i in range(5):
    for j in range(5):
        if classroom[i][j] == 'S':
            howmany_s += 1

ans = 0
for i in range(5):
    for j in range(5):
        if howmany_s < 4:
            break
        if classroom[i][j] == 'S':
            vis = [[0] * 5 for _ in range(5)]
            ans += dp(7, [(i, j)], 1)
            classroom[i][j] = 'A'
            howmany_s -= 1

print(ans)         