import sys
input = sys.stdin.readline

S = input().strip()
N = int(input())
A = [input().strip() for _ in range(N)]

def dp(w, words):
    if w in words:
        return 1
    l = len(w)
    subidx = 0
    for i in range(1, l+1):
        if w[0:i] in words:
            subidx = i
            if subidx == l:
                return 1
            else:
                ret = dp(w[subidx:], words)
                if ret == 1:
                    return 1

ret = dp(S, A)
print(1) if ret == 1 else print(0)