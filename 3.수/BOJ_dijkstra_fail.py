import math
import heapq

num_of_nodes, num_of_lines = map(int, input().split())
starting_node = int(input())

distances = [[10000000] * num_of_nodes for _ in range(num_of_nodes)]  #인접행렬로 짜면 메모리초과 -> 패착요인
vis = [0] * num_of_nodes #정점 방문 여부

for i in range(num_of_lines):
    s, d, w = map(int, input().split())
    if distances[s - 1][d - 1] > w:
        distances[s - 1][d - 1] = w

def dijkstra(start):
    distances[start - 1][start - 1] = 0
    vis[start - 1] = 1
    pq = []
    heapq.heappush(pq, (0, start - 1))
    while(len(pq) != 0):
        node_now = heapq.heappop(pq)
        for node in range(num_of_nodes):
            if (distances[node_now[1]][node] != 10000000) and (vis[node] == 0):
                heapq.heappush(pq,(distances[node_now[1]][node], node))
                if distances[start-1][node] > distances[start-1][node_now[1]] + distances[node_now[1]][node]:
                    distances[start-1][node] = distances[start-1][node_now[1]] + distances[node_now[1]][node]
        vis[node_now[1]] = 1

dijkstra(starting_node)
for n in range(num_of_nodes):
    if distances[starting_node-1][n] == 10000000:
        print("INF")
    else: 
        print(distances[starting_node-1][n])