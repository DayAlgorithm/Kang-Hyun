import sys
input = sys.stdin.readline
N, K = map(int, input().split())
win_lose = [list(map(int, input().split())) for _ in range(N)]
kh = list(map(int, input().split()))
mh = list(map(int, input().split()))

for i in range(20):
    kh[i] -= 1
    mh[i] -= 1

