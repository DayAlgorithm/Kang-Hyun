import sys
import heapq as hq
from collections import Counter
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    maxq = []
    minq = []
    entry_finder = Counter()
    for _ in range(k):
        cmd, num = input().rstrip().split()
        if cmd == 'I':
            hq.heappush(maxq, -int(num))
            hq.heappush(minq, int(num))
            entry_finder[int(num)] += 1
            continue
        elif cmd == 'D':
            if num == '1':
                while maxq:
                    val = -hq.heappop(maxq)
                    if entry_finder[val] > 0:
                        entry_finder[val] -= 1
                        break
            elif num == '-1':
                while minq:
                    val = hq.heappop(minq)
                    if entry_finder[val] > 0:
                        entry_finder[val] -= 1
                        break
    
    # maxq 정리
    while maxq and entry_finder[-maxq[0]] == 0:
        hq.heappop(maxq)

    # minq 정리
    while minq and entry_finder[minq[0]] == 0:
        hq.heappop(minq)
    
    #출력
    if sum(entry_finder.values()) > 0:
        maxval = -hq.heappop(maxq)
        minval = hq.heappop(minq)
        print(str(maxval) + " " + str(minval))
    else:
        print("EMPTY")