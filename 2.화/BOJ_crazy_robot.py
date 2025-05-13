n, pe, pw, ps, pn = map(int, input().split())
p_array = [pe/100, pw/100, ps/100, pn/100] #각 방향으로 갈 확률을 담은 배열
field = [[0] * (2*n+1) for _ in range(2*n+1)] #전체 필드는 동서남북으로 최대 n번 갈 수 있게 가로세로 2n+1 크기로 설정
direrctions = [[0,1,0], [0,-1,1], [1,0,2], [-1,0,3]] #방향, 맨 끝 요소는 그냥 순서임
now = [n, n] #초기 원점
field[n][n] = 1 #초가 원점 방문처리
results_sum = [0] #결과는 각 케이스 확률들의 합

def no_loop_counter(now, N, prob): #가능한 경로의 확률을 구하는 재귀함수. 
    #now는 현재위치, N은 이동횟수 카운터(역산), prob은 now에 오기까지 계속 곱해진 확률
    if N == 0: #n번 이동 -> 종료조건
        field[now[0]][now[1]] = 0 #현재위치 다시 미방문 처리
        results_sum[0] += prob #n번 이동할 동안 계산된 확률을 정답에 더함
        return
    for d in direrctions:
        next_y = now[0] + d[0] 
        next_x = now[1] + d[1] #다음 이동할 곳 설정
        if field[next_y][next_x] == 0: #다음 이동할 곳 검증 -> 방문을 아직 안한 곳인가?
            field[next_y][next_x] = 1 #방문하기로 한 뒤 방문처리
            no_loop_counter([next_y, next_x], N-1, prob * p_array[d[2]]) #다음위치, 횟수 카운터, 확률
    field[now[0]][now[1]] = 0 #다 방문했으면 현재위치 미방문처리
    return        

no_loop_counter(now, n, 1)
print(results_sum[0]) 