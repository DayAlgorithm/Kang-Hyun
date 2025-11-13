import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
destination = (N-1, N-1)
pipe_edge = (0,1)
pipe_state = "horizontal"

def find_number_of_paths(pipe_edge, pipe_state):
    number_of_paths = 0
    frame_queue = deque()
    frame_queue.append((pipe_edge, pipe_state))
    while(frame_queue):
        edge, state = frame_queue.pop()
        current_y, current_x = edge[0], edge[1]
       
        if current_y == N-1 and current_x == N-1:
            number_of_paths += 1
            continue
       
        if state == "horizontal":
            if current_x+1 < N and house[current_y][current_x+1] != 1:
                frame_queue.append(((current_y, current_x+1), "horizontal"))
            if current_x+1 < N and current_y+1 < N and house[current_y+1][current_x+1] != 1 and house[current_y][current_x+1] != 1 and house[current_y+1][current_x] != 1:
                frame_queue.append(((current_y+1, current_x+1), "diagonal"))
        
        if state == "vertical":
            if current_y+1 < N and house[current_y+1][current_x] != 1:
                frame_queue.append(((current_y+1, current_x), "vertical"))
            if current_x+1 < N and current_y+1 < N and house[current_y+1][current_x+1] != 1 and house[current_y][current_x+1] != 1 and house[current_y+1][current_x] != 1:
                frame_queue.append(((current_y+1, current_x+1), "diagonal"))
        
        if state == "diagonal":
            if current_x+1 < N and house[current_y][current_x+1] != 1:
                frame_queue.append(((current_y, current_x+1), "horizontal"))
            if current_y+1 < N and house[current_y+1][current_x] != 1:
                frame_queue.append(((current_y+1, current_x), "vertical"))
            if current_x+1 < N and current_y+1 < N and house[current_y+1][current_x+1] != 1 and house[current_y][current_x+1] != 1 and house[current_y+1][current_x] != 1:
                frame_queue.append(((current_y+1, current_x+1), "diagonal"))
    
    return number_of_paths

print(find_number_of_paths(pipe_edge, pipe_state))