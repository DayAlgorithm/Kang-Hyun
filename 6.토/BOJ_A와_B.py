import sys
input = sys.stdin.readline
S = list(input().strip())
T = list(input().strip())
for _ in range(len(T) - len(S)):
    if T[-1] == 'B':
        T.pop()
        T.reverse()
    else:
        T.pop()

if S == T:
    print(1)
else:
    print(0)
