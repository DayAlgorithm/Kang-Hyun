import sys
input = sys.stdin.readline
size = int(input())
m, n = map(int, input().split())
a = [int(input()) for _ in range(m)]
b = [int(input()) for _ in range(n)]

a_possible = {0:1}
b_possible = {0:1}

for i in range(m):
    asum = a[i]
    if asum in a_possible:
        a_possible[asum] += 1
    else:
        a_possible[asum] = 1
        
    for j in range(1, m-1):
        asum += a[(i+j)%m] 
        if asum in a_possible:
            a_possible[asum] += 1
        else:
            a_possible[asum] = 1
a_possible[sum(a)] = 1

for i in range(n):
    bsum = b[i]
    if bsum in b_possible:
        b_possible[bsum] += 1
    else:
        b_possible[bsum] = 1
        
    for j in range(1, n-1):
        bsum += b[(i+j)%n]
        if bsum in b_possible:
            b_possible[bsum] += 1
        else:
            b_possible[bsum] = 1
b_possible[sum(b)] = 1

ways = 0
for s in range(size + 1):
    if s in a_possible:
        way1 = a_possible[s]
        if size - s in b_possible:
            way2 = b_possible[size-s]
            ways += way1 * way2
    else:
        continue
    
print(ways)