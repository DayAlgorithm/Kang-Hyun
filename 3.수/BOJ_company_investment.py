N, M = map(int, input().split())
profits = [[0] * (M + 1)] + [list(map(int, input().split())) for _ in range(N)]
profit_table = [[[0] * (M + 1) for _ in range(N + 1)] for _ in range(M + 1)]  
#이익 표(dp)는 [최대이익, 1번째 회사 투자금액, 2번째 회사 투자금액, ..., n번째 투자금액] 이렇게 만들었다.
for company in range(1, M + 1): #iteration할 때마다 회사 하나씩 추가
    for invest in range(N, 0, -1): # 금액은 내림차순으로 순회
        maximum_profit = 0
        for partition in range(invest+1): # company개의 회사가 있을 때 invest 금액에서 최댓값을 구하기 위해 투자금액별 분할
            examine_profit = profits[partition][company] + profit_table[company-1][invest - partition][0] #partition이 company번째 회사 투자금 
            if maximum_profit <= examine_profit: 
                 maximum_profit = examine_profit
                 profit_table[company][invest] = list(profit_table[company-1][invest - partition]) # company-1 번째 회사의 투자방법에
                 profit_table[company][invest][company] = partition # company번째 회사의 투자금액(partition)을 덮어쓴다
                 profit_table[company][invest][0] = maximum_profit  # 최대이익 최신화해준다  
                 
print(profit_table[M][N][0])
how_to_invest = profit_table[M][N][1:]
print(*how_to_invest)
