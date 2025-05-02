num_of_balls = int(input())
balls = input()

#quicksort에서 피벗 쓰는 것에 영감을 받았음. 양쪽 공의 색이 바뀌는 지점을 왼쪽피벗, 오른쪽피벗으로 둠
#양쪽 피벗 찾기
piv_left = 0
piv_right = 0
previous_ball = balls[0]
for i in range(1, num_of_balls):
    if balls[i] != previous_ball:
        piv_left = i - 1
        break
    previous_ball = balls[i]
previous_ball = balls[-1]
for i in range(num_of_balls - 2, piv_left, -1):
    if balls[i] != previous_ball:
        piv_right = i + 1
        break
    previous_ball = balls[i]

#피벗들 사이의 볼 개수 찾기
red_balls = 0
for i in range(piv_left +1, piv_right):
    if balls[i] == "R":
        red_balls += 1

blue_balls = piv_right - piv_left - 1 - red_balls

balls_left = piv_left+1
balls_right = num_of_balls - piv_right

if piv_left == 0 and piv_right == 0: #모든 공이 같은 색
    answer = 0
elif balls[piv_left] == balls[piv_right]: #양 끝 공이 같은 색
    if balls[piv_left] == "R": #양 끝 공이 빨강
        if balls_left > balls_right:                #왼쪽에 공이 더 많은 경우
            if balls_right + red_balls > blue_balls: #파란 공 옯기는 경우
                answer = blue_balls
            else:
                answer = balls_right + red_balls
        else:                                       #오른쪽 공이 더 많음
            if balls_left + red_balls > blue_balls: #파란 공 옯기는 경우
                answer = blue_balls
            else:
                answer = balls_left + red_balls
    else: #양 끝 공이 파랑
        if balls_left > balls_right:                #왼쪽에 공이 더 많은 경우
            if balls_right + blue_balls > red_balls: #파란 공 옯기는 경우
                answer = red_balls
            else:
                answer = balls_right + blue_balls
        else:                                       #오른쪽 공이 더 많음
            if balls_left + blue_balls > red_balls: #파란 공 옯기는 경우
                answer = red_balls
            else:
                answer = balls_left + blue_balls       
else:    #양 끝 공 색이 다른 경우: 가운데 공만 비교
    if red_balls > blue_balls:
        answer = blue_balls
    else:
        answer = red_balls
        
print(answer)