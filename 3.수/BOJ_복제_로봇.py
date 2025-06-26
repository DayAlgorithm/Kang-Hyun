from collections import deque
import sys
input = sys.stdin.readline
size, keys = map(int, input().split())
maze = [list(input().strip()) for _ in range(size)]

# 시작점과 키 위치
start = []
keys_at = []
for s in range(size):
    for ss in range(size):
        if maze[s][ss] == 'S':
            start.append((s, ss))
        elif maze[s][ss] == 'K':
            keys_at.append((s, ss))
crucial = start + keys_at
pos_to_idx = {pos: i for i, pos in enumerate(crucial)} #좌표 - 인덱스 매핑

def BFS(startp):
    s_idx = crucial.index(startp)
    edges = [] #시작점에서 중요지점들까지의 최소거리 간선
    found = 0 # 찾은 간선 수
    
    dist = [[-1] * size for _ in range(size)]
    dist[startp[0]][startp[1]] = 0
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    
    q = deque()
    q.append(startp)
    
    while(q):
        cur = q.popleft()
        cy, cx = cur[0], cur[1]
        for d in directions:
            ny, nx = cy + d[0], cx + d[1]
            if ny >=0 and ny<size and nx>=0 and nx <size and maze[ny][nx] != '1':
                if dist[ny][nx] == -1: #방문하지 않은 곳
                    q.append((ny, nx))
                    dist[ny][nx] = dist[cy][cx] + 1
                    if maze[ny][nx] == 'K' or maze[ny][nx] == 'S':
                        idx = pos_to_idx[(ny, nx)]
                        if s_idx < idx: #중복 막기 위해 시작 정점이 도착 정점보다 작을 경우에만 간선 추가
                            edges.append((dist[ny][nx], s_idx, idx))
                        found += 1
    return found, edges


def find(n): #경로 압축 방식으로 find 구현
    if groups[n] < 0:
        return n
    else:
        groups[n] = find(groups[n])
        return groups[n]
        
    
all_edges = []    
for i in range(keys + 1):
    found, edges = BFS(crucial[i]) # (dist, i, j)
    if found != keys:
        print(-1)
        exit()
    for e in edges:
        all_edges.append(e)

#이제 MST 만들 차례임
MST = []
all_edges.sort()
groups = [-1] * (keys + 1) #초기엔 모든 정점의 루트가 자기 자신 == -1
for edge in all_edges:     #MST making...
    r1 = find(edge[1])
    r2 = find(edge[2])
    if r1 == r2:        #간선의 양 끝 정점이 같은 루트를 가지면 패스
        continue
    groups[edge[2]] = r1 #그렇지 않으면 union
    MST.append(edge)        #간선을 MST에 추가
    if len(MST) == keys:
        break
    
if len(MST) < keys:
    print(-1)
else:
    ans = 0
    for i in range(keys):
        ans += MST[i][0]
    print(ans)    