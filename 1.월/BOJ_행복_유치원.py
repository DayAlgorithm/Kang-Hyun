import sys
input = sys.stdin.readline

N, K = map(int, input().split())
kids = list(map(int, input().split()))
kids.sort()

# 인접한 차이 구하기
diff = []
for i in range(N-1):
    diff.append(kids[i+1] - kids[i])

# 큰 차이 K-1개 버리고 나머지 합
diff.sort(reverse=True)
answer = sum(diff[K-1:])
print(answer)