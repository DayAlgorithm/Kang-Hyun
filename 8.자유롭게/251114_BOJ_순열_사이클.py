import sys
sys.setrecursionlimit(10**6) 

input = sys.stdin.readline

def graph_crawler(node, vis, child):
    if vis[node] == 1:
        return
    vis[node] = 1
    if child[node] != node:
        graph_crawler(child[node], vis, child)

T = int(input())
for _ in range(T):
    N = int(input())
    child = [0] + list(map(int,input().split()))
    vis = [0] * (N+1)
    number_of_permutations = 0
    for node in range(1,N+1):
        if vis[node] == 0:
            graph_crawler(node, vis, child)
            number_of_permutations += 1
    print(number_of_permutations)