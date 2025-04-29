from collections import deque

def solution(n, computers):
    visited = [0] * n #방문여부
    queue = deque() #큐 사용
    networks = 0 #네트워크 숫자
    
    for j in range(n): 
        if visited[j] == 0: #안가본 곳 들어가기, bfs 구현
            queue.append(j)
            visited[j] = 1
            while len(queue) != 0:
                current_node = queue.popleft()
                for i in range(n):
                    if computers[current_node][i] == 1 and visited[i] == 0:
                        queue.append(i)
                        visited[i] = 1
            networks += 1 #안 가본 곳 들어가서 탐색 끝내면 네트워크 +=1
        
    answer = networks
    return answer