import sys
import bisect
input = sys.stdin.readline
N, H = map(int, input().split())
stalagmite = []
stalactite = []
for i in range(N):
    if i % 2 == 0:
        stalagmite.append(int(input()))
    else:
        stalactite.append(int(input()))
stalagmite.sort()
stalactite.sort()

stag_n = len(stalagmite)
stac_n = N - stag_n

altitude = [0 for _ in range(H+1)]

for i in range(1, H+1):
    hit_stags = stag_n - bisect.bisect_left(stalagmite, i)
    hit_stacs = stac_n - bisect.bisect_right(stalactite, H - i)
    altitude[i] += hit_stacs + hit_stags

minhits = N
alts = 0

for i in range(1, H+1):
    if minhits > altitude[i]:
        minhits = altitude[i]
        alts = 1
    elif minhits == altitude[i]:
        alts += 1

print(str(minhits) + " " + str(alts))