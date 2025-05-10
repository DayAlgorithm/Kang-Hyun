from collections import deque

t = int(input())
for case in range(t):
    n = int(input())
    last_year = list(map(int,input().split()))
    
    graph = [[False] * (n+1) for _ in range(n+1)]
    in_degree = [0] * (n+1)
    for i in range(n):
        for j in range(i+1,n):
            graph[last_year[i]][last_year[j]] = True
            in_degree[last_year[j]] += 1
    
    change = int(input())
    for i in range(change):
        t1, t2 = map(int,input().split())
        if graph[t1][t2]:
            graph[t1][t2] = False
            graph[t2][t1] = True
            in_degree[t1] += 1
            in_degree[t2] -= 1
        else:
            graph[t1][t2] = True
            graph[t2][t1] = False
            in_degree[t1] -= 1
            in_degree[t2] += 1
    
    result = []
    que = deque()
    impossible = False
    uncertain = False
    
    for i in range(1, n+1):
        if in_degree[i] == 0:
            que.append(i)
    
    for i in range(n):
        if len(que) == 0:
            impossible = True
            break
        if len(que) > 1:
            uncertain = True
            break
        now = que.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j] == True:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    que.append(j)
    if impossible:
        print("IMPOSSIBLE")
    elif uncertain:
        print("?")
    else:
        print(*result)