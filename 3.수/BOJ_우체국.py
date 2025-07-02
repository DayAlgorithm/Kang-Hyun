import sys
input = sys.stdin.readline
N = int(input())

villages = [list(map(int, input().split())) for _ in range(N)]
villages.sort()
total_men = 0
for i in range(N):
    total_men += villages[i][1]
    
halftotal_men = total_men / 2
subtotal_men = 0
ans = 0
for i in range(N):
    subtotal_men += villages[i][1]
    if subtotal_men >= halftotal_men:
        ans = villages[i][0]
        break
print(ans)