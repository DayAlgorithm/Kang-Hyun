import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
inf = 10001
maze = [list(map(int, input().split())) for _ in range(N)]
dist = [[inf] * M for _ in range(N)]

def bfs(start, ken, foundken):
    dist[start[0]][start[1]] = 0
    q = deque()
    q.append(start)
    ways = [(0,1), (0,-1), (1,0), (-1,0)]
    while(q):
        cur = q.popleft()
        cy, cx = cur[0], cur[1]
        for w in ways:
            ny, nx = cy + w[0], cx + w[1]
            if ny >= N or ny < 0 or nx >= M or nx < 0:
                continue
            if ken: #검 있는 경우
                if dist[ny][nx] > dist[cy][cx] + 1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    q.append((ny,nx))
            else: #없는 경우
                if maze[ny][nx] == 1: #벽 못감
                    continue
                if maze[ny][nx] == 2:
                    foundken = True
                if dist[ny][nx] > dist[cy][cx] + 1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    q.append((ny,nx))
    return foundken

ken = bfs((0,0), False, False)
no_ken_fastest = dist[N-1][M-1]
ken_fastest = inf

if ken:
    ken_at = (0,0)
    ken_dist = 0
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 2:
                ken_at = (i, j)
                ken_dist = dist[i][j]
                break

    dist = [[inf] * M for _ in range(N)]
    bfs(ken_at, ken, True)
    ken_fastest = ken_dist + dist[N-1][M-1]

ans = ken_fastest if ken_fastest < no_ken_fastest else no_ken_fastest
if ans <= T:
    print(ans)
else:
    print("Fail")            