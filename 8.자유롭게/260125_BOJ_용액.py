import sys
input = sys.stdin.readline
n = int(input())
solutions = list(map(int, input().split()))
ans1, ans2 = solutions[0], solutions[n-1]
ans_sum = abs(ans1 + ans2)
lo, hi = 0, n-1

while lo < hi:
    s1, s2 = solutions[lo], solutions[hi]
    cur_sum = s1 + s2
    if abs(cur_sum) < ans_sum:
        ans1, ans2 = s1, s2
        ans_sum = abs(cur_sum)
    if cur_sum < 0:
        lo +=1
    elif cur_sum == 0:
        break
    else:
        hi -= 1

print(ans1, ans2)