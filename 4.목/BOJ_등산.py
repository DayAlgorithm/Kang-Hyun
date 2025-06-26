import sys
import heapq as hq
input = sys.stdin.readline
N, M, T, D = map(int, input().split())
mountain = [list(input().strip()) for _ in range(N)]
tracks = [[] for _ in range(N)]
ways = [(-1,0), (0, 1), (1, 0), (0, -1)]
dist_go = [[-1] * M for _ in range(N)]
heights = []  # (높이, (좌표), 시간)

#  정점마다 북동남서의 간선을 저장
for i in range(N):
    for j in range(M):
        track = []
        for k in range(4):
            ty, tx = i + ways[k][0], j + ways[k][1]
            if ty < 0 or ty >= N or tx < 0 or tx >= M:
                track.append(-1)
            else:
                h, h2 = ord(mountain[i][j]), ord(mountain[ty][tx])
                h = h if h <= 90 else h - 6
                h2 = h2 if h2 <= 90 else h2 - 6
                d = h2 - h
                if d > T or d < -T:       # 등반 불가능 조건
                    track.append(-1)
                else:
                    track.append(d*d) if d > 0 else track.append(1)
        tracks[i].append(track)

def dijkstra(startp, dist, time): 
    dist[startp[0]][startp[1]] = 0
    h = [(0, startp)]
    
    while(h):
        cur = hq.heappop(h)
        cd, cy, cx = cur[0], cur[1][0], cur[1][1]
        if cd != dist[cy][cx] or cd >= time: #최단시간 / 제한시간
            continue
        for i in range(4):
            if tracks[cy][cx][i] == -1: # 해당 방형으로 갈 수 없는 경우(높이 또는 맵 크기제한)
                continue
            ny, nx = cy + ways[i][0], cx + ways[i][1]
            if dist[ny][nx] == -1 or dist[ny][nx] > cd + tracks[cy][cx][i]: #미방문/최단시간 조건
                dist[ny][nx] = cd + tracks[cy][cx][i]
                hq.heappush(h, (dist[ny][nx], (ny, nx)))

#다익스트라 수행해서 시작점부터 모든 정점의 최단거리(시간) 계산
dijkstra((0,0), dist_go, D)

for i in range(N):
    for j in range(M):
        if dist_go[i][j] == -1 or dist_go[i][j] >= D:
            continue
        hq.heappush(heights, (-ord(mountain[i][j]), (i, j), dist_go[i][j]))   # 최대 힙 이용, 가장 높은지점의 후보군들 지정
      
while True:
    test = hq.heappop(heights) #(높이, (좌표), 시간)
    time_left = D - test[2]
    if time_left < test[1][0] + test[1][1]: #남은 시간이 복귀의 가능한 최소시간보다 작을 경우 패스
        continue
    dist_back = [[-1] * M for _ in range(N)]
    dijkstra(test[1], dist_back, time_left)
    if dist_back[0][0] < 0:
        continue
    if dist_back[0][0] <= time_left:
        raw_char = -test[0]  # 원본 문자 
        if 65 <= raw_char <= 90:    # 대문자
            ans = raw_char - 65
        elif 97 <= raw_char <= 122: # 소문자
            ans = raw_char - 97 + 26
        print(ans)
        break