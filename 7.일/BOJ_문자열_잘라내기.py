import sys
input = sys.stdin.readline
r, c = map(int, input().split())
words = [input().rstrip() for _ in range(r)]

def check(point):
    seen = set()
    for i in range(c):
        word = ''.join(words[j][i] for j in range(point, r))
        if word in seen:
            return False
        else:
            seen.add(word)
    return True

lo, hi = 0, r-1
ans = 0
while lo<=hi:
    mid = (lo + hi) // 2
    if check(mid):
        ans = mid
        lo = mid+1
    else:
        hi = mid-1

print(ans)  