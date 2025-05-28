from collections import deque
T = int(input())
for i in range(T):
    N = int(input())
    points = [list(map(int,input().split())) for _ in range(N+2)]
    q = deque()
    q.append(points[0])
    #while(len(q) != 0):
