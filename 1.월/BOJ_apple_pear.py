from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tree = [[] for _ in range(n)]
for i in range(n):
    p, c = map(int, input())
    tree[p].append(c)

a_p = list(map(int, input().split()))

vis = [0 for _ in range(n)]
ans = [0, 0]
product = 0

stack = deque()
stack.append((0,1))

def bfs(start, visnum):
    while(len(stack) != 0):
        now, visnum = stack.pop()
        vis[now] = 1
        for n in tree[now]:
            if vis[n] == 0:
                stack.append((n, visnum+1))