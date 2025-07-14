import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
pool = [[[] for _ in range(C+1)] for _ in range(R+1)]
sharks = []
for _ in range(M):
    sharks.append([1] + list(map(int, input().split()))) #존재, 행, 열, 속도, 방향, 사이즈
#상어들, 수영장에 들어가다
for s in range(len(sharks)):
    pool[sharks[s][1]][sharks[s][2]].append((s, sharks[s][5])) #수영장에는 상어의 번호와 사이즈 기록

sum_size = 0
#낚시꾼, 이동하다
for c in range(1,C+1):
    
    #낚시꾼, 낚싯바늘을 던져넣다
    nearest_shark = [-1,-1,-1] #행 번호, 상어 번호, 상어 크기   
    for r in range(1,R+1):
        if len(pool[r][c]) != 0:
            nearest_shark[0] = r 
            nearest_shark[1] = pool[r][c][0][0]
            nearest_shark[2] = pool[r][c][0][1]
            break
    #낚시꾼, 상어를 낚다    
    if nearest_shark[0] != -1:
        #pool에서 상어 삭제
        pool[nearest_shark[0]][c].pop()
        #상어 배열에서 상어 리타이어
        sharks[nearest_shark[1]][0] = 0
        #잡은 크기에 추가  
        sum_size += nearest_shark[2]
    #상어들, 이동하다
    for shark in range(len(sharks)):
        s = sharks[shark]
        if s[0] == 0: #죽은 상어
            continue
        #이동한 후의 위치 계산, 그곳에 상어 저장
        dest = [-1, -1] #이동한 위치
        if s[4] == 1:
            dist = s[1] - 1 #벽까지의 거리
            if s[3] < dist: #벽까지 남은 거리가 속도보다 클 때
                dest = [s[1] - s[3], s[2]]
            elif s[3] == dist: #벽까지 남은 거리가 속도와 같을 때, 도착지는 벽
                dest = [1, s[2]]
                s[4] = 2        # 방향 바꿔줌
            else:           #벽까지 남은 거리가 속도보다 작을 때
                moves_left =  s[3] - dist   #일단 벽까지 이동했다고 침, 
                s[4] = 2                    #이제 방향은 반대
                if (moves_left // (R - 1)) % 2 == 0:
                    dest = [1 + moves_left % (R - 1), s[2]]
                else:
                    dest = [R - moves_left % (R - 1), s[2]]
                    s[4] = 1
        elif s[4] == 2:
            dist = R - s[1] #벽까지의 거리
            if s[3] < dist: #벽까지 남은 거리가 속도보다 클 때
                dest = [s[1] + s[3], s[2]]
            elif s[3] == dist: #벽까지 남은 거리가 속도와 같을 때, 도착지는 벽
                dest = [R, s[2]]
                s[4] = 1        # 방향 바꿔줌
            else:           #벽까지 남은 거리가 속도보다 작을 때
                moves_left =  s[3] - dist   #일단 벽까지 이동했다고 침, 
                s[4] = 1                    #이제 방향은 반대
                if (moves_left // (R - 1)) % 2 == 0:
                    dest = [R - moves_left % (R - 1), s[2]]
                else:
                    dest = [1 + moves_left % (R - 1), s[2]]
                    s[4] = 2
        elif s[4] == 3:
            dist = C - s[2] #벽까지의 거리
            if s[3] < dist: #벽까지 남은 거리가 속도보다 클 때
                dest = [s[1], s[2] + s[3]]
            elif s[3] == dist: #벽까지 남은 거리가 속도와 같을 때, 도착지는 벽
                dest = [s[1], C]
                s[4] = 4        # 방향 바꿔줌
            else:           #벽까지 남은 거리가 속도보다 작을 때
                moves_left =  s[3] - dist   #일단 벽까지 이동했다고 침, 
                s[4] = 4                    #이제 방향은 반대
                if (moves_left // (C - 1)) % 2 == 0:
                    dest = [s[1] ,C - moves_left % (C - 1)]
                else:
                    dest = [s[1], 1 + moves_left % (C - 1)]
                    s[4] = 3
        else:
            dist = s[2] - 1 #벽까지의 거리
            if s[3] < dist: #벽까지 남은 거리가 속도보다 클 때
                dest = [s[1], s[2] - s[3]]
            elif s[3] == dist: #벽까지 남은 거리가 속도와 같을 때, 도착지는 벽
                dest = [s[1], 1]
                s[4] = 3        # 방향 바꿔줌
            else:           #벽까지 남은 거리가 속도보다 작을 때
                moves_left =  s[3] - dist   #일단 벽까지 이동했다고 침, 
                s[4] = 3                    #이제 방향은 반대
                if (moves_left // (C - 1)) % 2 == 0:
                    dest = [s[1] ,1 + moves_left % (C - 1)]
                else:
                    dest = [s[1], C - moves_left % (C - 1)]
                    s[4] = 4
        #상어 dest에 저장하고, 원래 위치에서 삭제하기
        pool[dest[0]][dest[1]].append((shark, s[5]))
        if len(pool[s[1]][s[2]]) == 1:
            pool[s[1]][s[2]].pop()
        else:
            pool[s[1]][s[2]] = pool[s[1]][s[2]][1:]
        #shark 배열의 정보도 최신화
        s[1], s[2] = dest[0], dest[1]
    #상어들, 서로 먹고 먹히다
    for r in range(1,R+1):
        for cc in range(1,C+1):
            if len(pool[r][cc]) >= 2:
                max_size = 0
                max_shark = 0
                for s in pool[r][cc]:
                    if max_size < s[1]:
                        max_size = s[1]
                        max_shark = s[0]
                for s in pool[r][cc]:
                    if s[1] != max_size:
                        sharks[s[0]][0] = 0 #잡아먹히다
                pool[r][cc] = [(max_shark, max_size)] # 잡아 먹은 상어만 남는다.

print(sum_size)