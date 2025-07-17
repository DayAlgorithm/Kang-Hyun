import sys
import heapq
input = sys.stdin.readline

def dijkstra(startp, room, dist):
    height = len(room)
    width = len(room[0])
    direc = [(1,0), (-1,0), (0,1), (0,-1)]
    h = [(0,startp)]
    dist[startp[0]][startp[1]] = 0
    while(h):
        cur = heapq.heappop(h)
        cd, cy, cx = cur[0], cur[1][0], cur[1][1]
        if cd != dist[cy][cx]:
            continue
        for d in direc:
            ny, nx = cy + d[0], cx + d[1]
            if ny < 0 or ny >= height or nx<0 or nx>=width:
                continue
            if room[ny][nx] == 'x':
                continue
            if dist[ny][nx] == -1 or dist[ny][nx] > cd +1:
                dist[ny][nx] = cd + 1
                heapq.heappush(h, (cd+1, (ny, nx)))
    
while(True):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    room = [list(input().strip()) for _ in range(h)]
    robot = (0,0)
    dirts = []
    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':
                robot = (i,j)
            elif room[i][j] == '*':
                dirts.append((i,j))

    moves = 0
    for i in range(len(dirts)):         #먼지 수만큼 반복
        dist = [[-1] * w for _ in range(h)]
        dijkstra(robot, room, dist)     #현재 로봇 위치에서 다익스트라
        closest_dirt = dirts[0]         #가장 가까운 먼지
        didx = 0                        #가장 가까운 먼지의 인덱스
        
        for dirt in range(len(dirts)):  
            d = dirts[dirt]
            if dist[d[0]][d[1]] == -1:  #닿을 수 없는 먼지 존재
                moves = -1
                break
            elif dist[d[0]][d[1]] < dist[closest_dirt[0]][closest_dirt[1]]: #가장 가까운 먼지 갱신
                closest_dirt = d
                didx = dirt
        if moves == -1:
            break
        
        robot = closest_dirt            #가장 가까운 먼지의 위치로 로봇 이동
        moves += dist[closest_dirt[0]][closest_dirt[1]]
        dirts = dirts[:didx] + dirts[didx+1:]
        
    print(moves)