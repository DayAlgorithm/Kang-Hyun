import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
shark_size = 2
ate = 0
place = (0,0)
edible = [[] for _ in range(N)]
T = 0

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            place = (i, j)
            break

def bfs(start, size):
    dist[start[0]][start[1]] = 0
    q = deque()
    q.append(start)
    ways = [(0,1), (0,-1), (1,0), (-1,0)]
    while(q):
        cur = q.popleft()
        cy, cx = cur[0], cur[1]
        for w in ways:
            ny, nx = cy + w[0], cx + w[1]
            if ny >= N or ny < 0 or nx >= N or nx < 0:
                continue
            if sea[ny][nx] > size:
                continue
            if dist[ny][nx] == -1 or dist[ny][nx] > dist[cy][cx] + 1:
                dist[ny][nx] = dist[cy][cx] + 1
                q.append((ny,nx))
                
while(True):
    dist = [[-1] * N for _ in range(N)]
    bfs(place, shark_size)
    ##
    print(dist)
    ##
    min_dist = N * N
    next_place = (0,0)
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 0 or sea[i][j] == 9 or sea[i][j] == shark_size:
                continue
            if dist[i][j] != -1 and min_dist > dist[i][j]:
                min_dist = dist[i][j]
    if min_dist == N * N:
        break
    
    for i in range(N):
        for j in range(N):
            if dist[i][j] == min_dist:
                if sea[i][j] != 0 and sea[i][j] != 9:
                    next_place = (i, j)
                    break
    sea[place[0]][place[1]] = 0
    sea[next_place[0]][next_place[1]] = 9
    place = next_place    
    T += min_dist
    ate += 1
    if ate == shark_size:
        shark_size += 1
        ate = 0
    ##
    print(sea)
    ##

print(T)