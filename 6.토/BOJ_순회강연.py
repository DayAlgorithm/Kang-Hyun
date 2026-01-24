import sys
import heapq as hq

input = sys.stdin.readline
n = int(input())

seminars = []
selected = []
selected_n = 0

for _ in range(n):
    p, d = map(int, input().split())
    seminars.append((d, p))

seminars = sorted(seminars) #날짜 오름차순 정렬

for s in seminars:
    if selected_n < s[0]: #현재 아이템의 날짜보다 선택된 개수가 적을 경우
        hq.heappush(selected, (s[1], s[0]))
        selected_n += 1
    else:                   #현재 아이템의 날짜와 선택된 개수가 같을 경우(클 경우는 정렬 떄문에 없음)
        lowest_select = hq.heappop(selected)
        if s[1] > lowest_select[0]:
            hq.heappush(selected, (s[1], s[0]))
        else:
            hq.heappush(selected, lowest_select)

ans = 0
for s in selected:
    ans += s[0]
print(ans)