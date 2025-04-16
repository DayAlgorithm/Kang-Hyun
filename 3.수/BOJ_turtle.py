import sys
num = int(input())
cases = sys.stdin.read().splitlines()


mov = [(0,1), (1,0), (0,-1), (-1,0)]
result = []

for case in cases:
    turtle = [0, 0]
    turtle_x_min = 0
    turtle_x_max = 0
    turtle_y_min = 0
    turtle_y_max = 0
    mov_index =0
    for command in case:
        if command == 'R':
            mov_index = (mov_index + 1) % 4
        elif command == 'L':
            mov_index = (mov_index - 1) % 4
        elif command == 'F':
            turtle[0] += mov[mov_index][0]
            turtle[1] += mov[mov_index][1] 
        else:
            turtle[0] -= mov[mov_index][0]
            turtle[1] -= mov[mov_index][1]
        
        if turtle[0] > turtle_x_max:
            turtle_x_max = turtle[0]
        elif turtle[0] < turtle_x_min:
            turtle_x_min = turtle[0]
            
        if turtle[1] > turtle_y_max:
            turtle_y_max = turtle[1]
        elif turtle[1] < turtle_y_min:
            turtle_y_min = turtle[1]
    
    result.append((turtle_y_max - turtle_y_min) * (turtle_x_max - turtle_x_min)) 

for r in result:
    print(r)