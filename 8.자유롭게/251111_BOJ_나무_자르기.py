import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

tall = max(trees)
short = 0
ans = tall

while(short <= tall):
    cut = (short + tall) // 2
    total_length = 0
    for t in trees:
        if t > cut:
            total_length += t - cut
        if total_length >= M:
            break
    if total_length >= M:
        ans = cut
        short = cut + 1
    else:
        tall = cut - 1

print(ans)