R, C, T = map(int, input().split())
room = [list(map(int,input().split())) for _ in range(R)]

purifier = []
for i in range(R):
    if room[i][0] == -1:
        purifier = [i, i+1] #이 배열엔 공기청정기의 y값을 담음.
        break

for t in range(T):
    spread = [[0] * C for _ in range(R)] #확산된 값을 합산하고 나중에 room에 다시 복사할 것임.
    for r in range(R):
        for c in range(C):
            if room[r][c] != 0 and room[r][c] != -1:  # 확산 구현
                count = 0
                spr = room[r][c] // 5 #확산치
                if r+1 < R: #아래로 확산하는 경우
                    if c != 0: #아래가 공기청정기일 수 없는 케이스
                        spread[r+1][c] += spr
                        count += 1
                    elif r+1 != purifier[0]: #아래가 공기청정기일 수도 있어서 아닌 걸 체크
                        spread[r+1][c] += spr
                        count += 1
                if r-1 >= 0: # 위로 확산하는 경우, 세부 로직은 아래로 확산하는 경우와 동일
                    if c != 0:
                        spread[r-1][c] += spr
                        count += 1
                    elif  r-1 != purifier[1]:
                        spread[r-1][c] += spr
                        count += 1
                if c+1 < C: # 오른쪽 확산, 이 경우엔 공기청정기 쪽으로 확산하지 않음. 제일 간단.
                    spread[r][c+1] += spr
                    count += 1
                if c-1 >= 0: # 왼쪽 확산, 세부 논리는 아래/위 확산과 같음.
                    if c-1 !=0:
                        spread[r][c-1] += spr
                        count += 1
                    elif r != purifier[0] and r != purifier[1]:
                        spread[r][c-1] += spr
                        count += 1
                spread[r][c] += room[r][c] - count*spr  #이제 확산한 만큼 빼준 값을 원래 자리에 더해줌      
    for r in range(R):
        for c in range(C):
            room[r][c] = spread[r][c] #확산 배열을 room으로 복사
    
    #공기청정 시작
    room[purifier[0]][0] = 0 
    room[purifier[1]][0] = 0 #공기청정기의 자리는 0으로 만들어서 -1이 다른 자리로 가지 않게 함.
    #위쪽 공청기 순환
    for i in range(purifier[0]-1, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(0, C-1):
        room[0][i] = room[0][i+1]
    for i in range(0, purifier[0]):
        room[i][C-1] = room[i+1][C-1]
    for i in range(C-1, 0, -1):
        room[purifier[0]][i] = room[purifier[0]][i-1]
    #아랫쪽 공청기 순환
    for i in range(purifier[1]+1, R-1):
        room[i][0] = room[i+1][0]
    for i in range(0, C-1):
        room[R-1][i] = room[R-1][i+1]
    for i in range(R-1, purifier[1], -1):
        room[i][C-1] = room[i-1][C-1]
    for i in range(C-1, 0, -1):
        room[purifier[1]][i] = room[purifier[1]][i-1]
    #공기청정기 되돌려놓기
    room[purifier[0]][0] = -1
    room[purifier[1]][0] = -1
 
remaining = 0   #남은 먼지
for r in range(R):
    for c in range(C):
        if room[r][c] == -1:
            continue
        remaining += room[r][c] # 합산
print(remaining) #답!