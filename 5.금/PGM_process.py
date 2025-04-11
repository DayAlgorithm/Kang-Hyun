from collections import deque
def solution(priorities, location):
    idx = 0   # location과 비교할 녀석
    priorities_and_loc = [] # 우선순위, 원하는 프로세스의 위치 표시
    sorted_priorities = sorted(priorities, reverse=True) # 우선순위 추적을 위해
    
    for priority in priorities:
        if idx == location: # 우리가 원하는 프로세스
            priorities_and_loc.append((priority, 1)) #원하는 프로세스 -> 두번째 값이 1
            idx += 1
            continue
        priorities_and_loc.append((priority, 0)) #나머지 프로세스 -> 두번째 값 0
        idx += 1
    
    queue = deque(priorities_and_loc) # 앞서 만든 배열을 deque로 바꿔줌
    cnt = 0 # 실행 순서를 계산하기 위함
    
    while len(queue) > 0:
        prior_num, is_loc = queue.popleft() #우선순위, 원하는 프로세스인지
        if prior_num == sorted_priorities[cnt]: #현재 pop의 우선순위와 최대 우선순위 비교
            if is_loc == 1: # 원하는 프로세스
                cnt += 1 
                break #종료
            cnt += 1 
            continue
        queue.append((prior_num, is_loc)) #최대 우선순위 아니면 다시 넣기
        
    answer = cnt
    return answer