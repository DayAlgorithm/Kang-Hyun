n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]

recipe_founded = [True] * (n+1) #기본 부품으로 분해한 결과가 저장되어있는지 여부

for i in range(m):
    x, y, k = map(int, input().split())
    graph[x][y] = k
    recipe_founded[x] = False #기본 부품 외에는 모두 거짓

for i in range(1,n+1):
    if recipe_founded[i] == True:
        graph[i][i] = 1 # 기본 부품인 경우 자기 자신만 필요하므로
    
def dp(part):
    # 완전히 분해해보았는지를 확인하고 그러면 저장된 값 사용, 아니면 분해
    if recipe_founded[part]:
        return
    for i in range(1, part):
        if graph[part][i] != 0:
            how_many = graph[part][i]
            graph[part][i] = 0
            dp(i)
            for j in range(1, n+1):
                graph[part][j] += graph[i][j] * how_many
    recipe_founded[part] = True

dp(n)

for i in range(1, n+1):
    if graph[n][i] != 0:
        print(i, graph[n][i])