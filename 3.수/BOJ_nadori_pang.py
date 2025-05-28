N, K, T = map(int, input().split())
basket = list(map(int, input().split()))
basket = sorted(basket)
nadoris = sum(basket)
max_index = N-1
min_index = 0
for i in range(N):
    if basket[i] != 0:
        min_index = i
        break        

if nadoris % K == 0:
    while(T > 0):
        basket[min_index] -= 1
        basket[max_index] += 1
        if basket[min_index] == 0:
            min_index += 1
        if basket[max_index] == K:
            basket[max_index] = 0
            max_index -= 1   
        if max_index <= min_index:
            break     
        T-=1
    are_all_gone = all(num==0 for num in basket)
    if are_all_gone:
        print("YES")
    else:
        print("NO")
else:
    print("NO")