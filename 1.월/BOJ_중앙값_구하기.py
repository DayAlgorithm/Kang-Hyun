import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M = int(input())
    arr = []
    get_times = M // 10 + 1
    
    for i in range(get_times):
        arr += list(map(int,input().split()))
    
    sarr = []
    medians = []
    odd = True
    
    for m in range(M):
        sarr.append(arr[m])
        if odd:
            sarr.sort()
            medians.append(sarr[m // 2])
        odd = not odd
    
    print_times = (M // 2 + 1) // 10 + 1
    print(M//2 + 1)
    for i in range(print_times):
        print(' '.join(map(str, medians[10 * i: 10 * (i + 1)])))