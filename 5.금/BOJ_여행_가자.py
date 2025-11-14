import sys
import copy
input = sys.stdin.readline
N = int(input())
M = int(input())

first_city = list(map(int, input().split()))
city_sets = [set([1]) | set([i+1 for i in range(N) if first_city[i] == 1])]
for i in range(1, N):
    ith_city_linked = list(map(int, input().split()))
    ith_city_set = set([i+1]) | set([i+1 for i in range(N) if ith_city_linked[i] == 1])
    
    no_intersection = True
    for j in range(len(city_sets)):
        if city_sets[j] & ith_city_set:
            city_sets[j] = city_sets[j].union(ith_city_set)
            no_intersection = False
    if no_intersection:
        city_sets.append(ith_city_set)

final_city_sets = copy.deepcopy(city_sets)
for i in range(len(city_sets)):
    for j in range(i+1, len(city_sets)):
        if final_city_sets[i] & city_sets[j]:
            final_city_sets[i] = final_city_sets[i].union(city_sets[j])

ans = "NO"
city_want_to_visit = set(list(map(int, input().split())))
for city_set in final_city_sets:
    if city_want_to_visit - city_set:
        continue
    else:
        ans = "YES"
        break
print(ans)