v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
for i in range(e):
    x, y, w = map(int, input().split())
    graph[x].append([w,y])
INF = 10000000
dist = [INF] * (v+1)
dist[k] = 0


