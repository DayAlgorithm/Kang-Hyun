import sys
import heapq
input = sys.stdin.readline

N = int(input())

road = [tuple(map(int, input().split())) for _ in range(N)]
vil, gas = map(int, input().split())
road.append((vil, 0))
road.sort()
stops = 0
gas -= road[0][0]

passed = []
for i in range(0, N):
    heapq.heappush(passed, -road[i][1]) #일단 연료통 기억
    to_go = road[i+1][0] - road[i][0]
    while (to_go > gas) : #다음으로 갈 만큼의 연료가 없으면 
        if len(passed) == 0:
            print(-1)
            exit()
        g = -heapq.heappop(passed)
        gas += g
        stops += 1
    gas -= to_go
print(stops)            