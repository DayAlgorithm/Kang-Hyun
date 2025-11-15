import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K, M, P = map(int, input().split())
    graph = [[] for _ in range(M+1)]
    indegree = [0] * (M+1)

    for _ in range(P):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    order = [0] * (M+1)
    cnt = [0] * (M+1)

    q = deque()

    # indegree == 0 → Strahler = 1
    for i in range(1, M+1):
        if indegree[i] == 0:
            order[i] = 1
            cnt[i] = 1
            q.append(i)

    while q:
        cur = q.popleft()
        
        for nxt in graph[cur]:
            if order[cur] > order[nxt]:
                order[nxt] = order[cur]
                cnt[nxt] = 1
            elif order[cur] == order[nxt]:
                cnt[nxt] += 1
            
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                if cnt[nxt] >= 2:
                    order[nxt] += 1
                q.append(nxt)

    print(K, order[M])
