import sys
input = sys.stdin.readline
N = int(input())
cost_of_colors = [list(map(int,input().split())) for _ in range(N)]
lowest_costs = [[0]*3 for _ in range(N)]
lowest_costs[0] = cost_of_colors[0][:]

for i in range(1, N):
    lowest_costs[i][0] = cost_of_colors[i][0] + min(lowest_costs[i-1][1], lowest_costs[i-1][2])
    lowest_costs[i][1] = cost_of_colors[i][1] + min(lowest_costs[i-1][0], lowest_costs[i-1][2])
    lowest_costs[i][2] = cost_of_colors[i][2] + min(lowest_costs[i-1][0], lowest_costs[i-1][1])

print(min(lowest_costs[-1]))