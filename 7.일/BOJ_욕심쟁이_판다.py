import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

bamboo = [list(map(int, input().split())) for _ in range(n)] # 대숲
vis = [[0] * n for _ in range(n)] #방문기록 겸 해당 지점 출발 시 도달가능한 최대 거리
direc = [(1,0), (0,1), (-1,0), (0,-1)] #방향

def dfs(cur):
    cy, cx = cur[0], cur[1] #현재 좌표
    depth = 1 
    vis[cy][cx] = 1 #현재지점 일단 방문처리
    
    for d in direc:
        ny, nx = cy +d[0], cx + d[1] #다음 좌표 후보
        if ny <0 or ny >= n or nx <0 or nx >= n:
            continue
        if bamboo[ny][nx] <= bamboo[cy][cx]: #다음 좌표의 대나무가 더 적으면 패스
            continue
        if vis[ny][nx] == 0:        #방문기록이 없으면 일단 방문
            depth = max(depth, 1+ dfs((ny,nx))) #방문했을때 얻어낼 수 있는 깊이
        else:
            depth = max(depth, 1 + vis[ny][nx])
                
    vis[cy][cx] = depth
    return depth

for i in range(n):
    for j in range(n):
        if vis[i][j] == 0:
            dfs((i, j))

max_depth = 1
for i in range(n):
    for j in range(n):
        if max_depth < vis[i][j]:
             max_depth = vis[i][j]
print(max_depth)