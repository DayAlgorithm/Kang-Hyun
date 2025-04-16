import sys
num = int(input())
cases = sys.stdin.read().splitlines()


mov = [(0,1), (1,0), (0,-1), (-1,0)] #바라보는 방향 : 북, 동, 남, 서
result = [] # 결과 저장용 배열

for case in cases:
    turtle = [0, 0]  #케이스마다 거북이 위치 초기화
    turtle_x_min = 0 #x 최솟값
    turtle_x_max = 0 #x 최댓값
    turtle_y_min = 0 #y 최솟값
    turtle_y_max = 0 #y 최댓값
    mov_index = 0 #바라보는 방향 배열의 인덱스 값 초기화
    for command in case:
        if command == 'R':
            mov_index = (mov_index + 1) % 4 #R이면 시계방향 90도
        elif command == 'L':
            mov_index = (mov_index - 1) % 4 #L이면 반시계 90도
        elif command == 'F':
            turtle[0] += mov[mov_index][0] #F면 바라보는 방향의 +1연산
            turtle[1] += mov[mov_index][1] 
        else:
            turtle[0] -= mov[mov_index][0] #B면 바라보는 방향의 -1연산
            turtle[1] -= mov[mov_index][1]
        
        if turtle[0] > turtle_x_max: #x방향 이동범위
            turtle_x_max = turtle[0]
        elif turtle[0] < turtle_x_min:
            turtle_x_min = turtle[0]
            
        if turtle[1] > turtle_y_max: #y방향 이동범위
            turtle_y_max = turtle[1]
        elif turtle[1] < turtle_y_min:
            turtle_y_min = turtle[1]
    
    result.append((turtle_y_max - turtle_y_min) * (turtle_x_max - turtle_x_min)) #직사각형 넓이

for r in result:
    print(r)
