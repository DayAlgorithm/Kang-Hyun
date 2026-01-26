import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]

max_side = 0

for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and matrix[i][j] == 1:
            matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        if matrix[i][j] > max_side:
            max_side = matrix[i][j]

print(max_side ** 2)