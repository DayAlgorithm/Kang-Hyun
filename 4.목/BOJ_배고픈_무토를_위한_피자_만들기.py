import sys
input = sys.stdin.readline
N = int(input())
init_r, init_c = map(int,input().split())

pizza = [["."] * N for _ in range(N)]
pizza[init_r - 1][init_c - 1] = "#"

wanted = [list(input().strip()) for _ in range(N)]


