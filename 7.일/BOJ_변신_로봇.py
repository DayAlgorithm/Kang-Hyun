import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
parts = [[]] #0번째 인덱스는 dummy

for _ in range(N):
    parts.append(list(input().strip())) #문자열로 상태별 각 부품 입력받기

parts_len = len(parts[1]) # 상태 하나가 가지는 부품의 수
for i in range(1, N+1):
    for p in range(parts_len):
        parts[i][p] = int(parts[i][p]) #부품을 문자열에서 정수로 변환
        
initial, want = map(int, input().split()) #초기상태, 원하는 상태

shortest = [-1] * (N+1)
def dijkstra(startp):
    shortest[startp] = 0
    q = [(0, startp)]
    while(q):
        cd, cp = hq.heappop(q)
        if shortest[cp] != cd:
            continue
        for stat in range(1, N+1):
            length = 0
            for part in range(parts_len):
                length += ((parts[stat][part] - parts[cp][part]) ** 2)
            if shortest[stat] == -1 or shortest[stat] > cd + length:
                shortest[stat] = cd + length
                hq.heappush(q, (shortest[stat], stat))

dijkstra(initial)
print(shortest[want])