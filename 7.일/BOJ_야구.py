import sys
from collections import deque
input = sys.stdin.readline
N = int(input()) #2~50
future = [list(map(int, input().split())) for _ in range(N)] #(0~N) * (0~8)
sequence = []   #2~9
best_score = [0]
visited = [False] * 10

def backtrack():
    if len(sequence) == 8:
        sequence_made = sequence[:3] + [1] + sequence[3:] 
        score = calculate_score(sequence_made)
        if best_score[0] < score:
            best_score[0] = score
        return
    for i in range(2, 10): #2번 선수부터 9번 선수까지
        if not visited[i]:
            sequence.append(i)
            visited[i] = True
            backtrack()
            sequence.pop()
            visited[i] = False

def calculate_score(sequence_made):
    inning = 0
    total_score = 0
    hit_turn = 0
    while inning < N:
        b1, b2, b3 = 0, 0, 0
        outs = 0
        while outs < 3:
            hit_score = future[inning][sequence_made[hit_turn]-1]
            if hit_score == 0:
                outs += 1
            elif hit_score == 1:
                total_score += b3
                b1, b2, b3 = 1, b1, b2
            elif hit_score == 2:
                total_score += b2+b3
                b1, b2, b3 = 0, 1, b1
            elif hit_score == 3:
                total_score += b1+b2+b3
                b1, b2, b3 = 0, 0, 1
            else:
                total_score += b1+b2+b3+1
                b1, b2, b3 = 0, 0, 0
            hit_turn = (hit_turn + 1) % 9
        inning += 1
    return total_score

backtrack()
print(best_score[0])