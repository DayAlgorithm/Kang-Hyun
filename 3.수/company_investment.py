N, M = map(int, input().split())
profits = [[0] * (M + 1)] + [list(map(int, input().split())) for _ in range(N)]
profit_table = [[[0] * (M + 1) for _ in range(N + 1)] for _ in range(M + 1)]

for company in range(1, M + 1):
    for invest in range(N, 0, -1):
        maximum_profit = 0
        for partition in range(invest+1):
            examine_profit = profits[partition][company] + profit_table[company-1][invest - partition][0]
            if maximum_profit <= examine_profit:
                 maximum_profit = examine_profit
                 profit_table[company][invest] = list(profit_table[company-1][invest - partition])
                 profit_table[company][invest][company] = partition
                 profit_table[company][invest][0] = maximum_profit    
                 
print(profit_table[M][N][0])
how_to_invest = profit_table[M][N][1:]
print(*how_to_invest)