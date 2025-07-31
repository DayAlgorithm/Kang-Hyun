import sys
import heapq as hq
input = sys.stdin.readline
N, M = map(int, input().split())
bulb_comb = {}

#  열의 조합과 개수를 딕셔너리로 저장 -> 같이 켜지고 꺼지려면 열 조합이 같아야 함
for _ in range(N):
    bulb_row = input().rstrip()
    if bulb_row in bulb_comb:
        bulb_comb[bulb_row] += 1
    else:
        bulb_comb[bulb_row] = 1

#우순큐로 다시 저장
bulbs = []
for k, v in bulb_comb.items():
    hq.heappush(bulbs, (-v, k))
    
K = int(input())
best = 0

while(bulbs):
    comb_num, comb = hq.heappop(bulbs)
    clicks = 0 # 열 조합에서 켜야 하는 전구의 개수
    for i in range(len(comb)):
        if comb[i] == '0':
            clicks += 1
    if clicks <= K and (K - clicks) % 2 == 0: #다 켜는 게 가능한 조합인지
        if best < -comb_num:
            best = -comb_num
    else:
        continue        
    
print(best)