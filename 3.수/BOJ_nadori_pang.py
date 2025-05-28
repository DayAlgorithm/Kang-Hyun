N, K, T = map(int, input().split())
basket = list(map(int, input().split()))
basket = sorted(basket) #바구니 정렬
nadoris = sum(basket) #총 나도리
max_index = N-1 #최대 나도리 바구니 위치
min_index = 0
for i in range(N):
    if basket[i] != 0:
        min_index = i #0보다 큰 최소 나도리 바구니 위치
        break        

if nadoris % K == 0: #포인터 두개 앞뒤로 갱신하며 반복
    while(T > 0):
        basket[min_index] -= 1 #최소에서 하나 빼서
        basket[max_index] += 1 #최대에 줌
        if basket[min_index] == 0: #최소가 0 되면 최소위치 갱신
            min_index += 1
        if basket[max_index] == K: #최대가 K되면 최대 위치 갱신
            basket[max_index] = 0
            max_index -= 1   
        if max_index <= min_index: #두개 교차하거나 같으면 조기종료
            break     
        T-=1 
    are_all_gone = all(num==0 for num in basket) # 다 0인지 확인
    if are_all_gone:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
