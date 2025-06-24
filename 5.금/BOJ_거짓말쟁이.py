import sys
input = sys.stdin.readline

N = int(input())
table = input().strip().split()
least_liar = N+1

def dp(honesty, psuedo_opinion, start, end, current_liars):
    if honesty: #진실을 말하는 사람이 ?라 답함
        if psuedo_opinion == "L": # ?가 L라 가정-> 다음 사람 거짓말쟁이
            honesty = False
            current_liars += 1
            for k in range(start+1, end):
                if honesty and table[k] == "L":
                    honesty = False
                    current_liars += 1
                elif (not honesty) and table[k] == "H":
                    current_liars+=1
                else:
                    honesty = True
                    
    else:
                    
                    
    return 0



#assume that ith person is honest
for i in range(N):
    honest, liar = 1, 0 
    honesty = True
    this_liars = -1
    for j in range(-N + i, i-1):
        if honesty:
            if table[j] == "H":
                honest += 1
            elif table[j] == "L":
                liar += 1
                honesty = False
        else:
            if table[j] == "H":
                liar += 1
            elif table[j] == "L":
                honest += 1
                honesty = True
    #가정에 따라, 마지막 사람이 i번째 사람이 진실을 말함을 진술할 경우, 우리의 계산은 유효    
    if honesty and table[i-1] == "H":           
        this_liars = liar
    elif (not honesty) and table[i-1] == "F":
        this_liars = liar 
           
    if this_liars == -1:   # ith person honest 가 안되는 경우(무효)
        continue 
    else:                  # 유효한 경우, 결과를 비교 후 최소이면 반영
        if least_liar > this_liars:
            least_liar = this_liars
    
#assume that ith person is a liar    
for i in range(N):
    honest, liar = 0, 1
    honesty = False
    this_liars = -1
    for j in range(-N + i, i-1):
        if honesty:
            if table[j] == "H":
                honest += 1
            elif table[j] == "L":
                liar += 1
                honesty = False
        else:
            if table[j] == "H":
                liar += 1
            elif table[j] == "L":
                honest += 1
                honesty = True
    #가정에 따라, 마지막 사람이 i번째 사람이 거짓을 말함을 진술할 경우, 우리의 계산은 유효    
    if honesty and table[i-1] == "F":           
        this_liars = liar
    elif (not honesty) and table[i-1] == "H":
        this_liars = liar 
           
    if this_liars == -1:   # ith person liar 가 안되는 경우(무효)
        continue 
    else:                  # 유효한 경우, 결과를 비교 후 최소이면 반영
        if least_liar > this_liars:
            least_liar = this_liars        
     
print(least_liar)         