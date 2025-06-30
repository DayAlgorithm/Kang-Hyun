import sys
input = sys.stdin.readline
N, M = map(int, input().split())
i, j, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
direction = [(-1,0), (0,1), (1,0), (0,-1)]

def robot(cur, curd):
    cleaned = 0
    
    while True:
        if room[cur[0]][cur[1]] == 0:
            room[cur[0]][cur[1]] = 2
            cleaned += 1
        
        clean = True
        
        for d in direction:
            ny, nx = cur[0] + d[0], cur[1] + d[1]
            if room[ny][nx] == 0:
                clean = False
                
        if clean:
            by, bx = cur[0] - direction[curd][0], cur[1] - direction[curd][1]
            if room[by][bx] == 1:
                return cleaned
            else:
                cur = (by, bx)
        else:
            curd = (curd - 1) % 4
            fy, fx = cur[0] + direction[curd][0], cur[1] + direction[curd][1]
            if room[fy][fx] == 0:
                cur = (fy, fx)
                    

print(robot((i, j), d))       