import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
vis = [[0] * M for _ in range(N)]
direction = [[1,0], [0,1], [-1, 0], [0, -1]]

start = [0, 0, 1]
stack = deque()
stack.append(start)
ans = [N * M]

def bfs():
    while (stack):
       now = stack.popleft()
       y, x, cnt = now[0], now[1], now[2]
       
       if y == N-1 and x == M-1:
          if ans[0] > cnt:
              ans[0] = cnt 
          continue  
       for i in range(4):
           ny = y + direction[i][0]
           nx = x + direction[i][1]
           if ny >= N or nx >= M or ny < 0 or nx < 0:
               continue
           if maze[ny][nx] == 1 and vis[ny][nx] == 0:
               vis[ny][nx] = 1
               stack.append([ny, nx, cnt+1])
               
bfs()
print(ans[0])               