import sys
input = sys.stdin.readline
N = int(input())
points = list(map(int, input().split()))
sorted_points = sorted(points)
point_to_order = {}
point_to_order[sorted_points[0]] = 0
point_before = sorted_points[0]
order = 1
for point in sorted_points[1:]:
    if point == point_before:
        point_before = point
        continue
    point_to_order[point] = order
    point_before = point
    order += 1
ans = []
for point in points:
    ans.append(point_to_order[point])
print(" ".join(map(str,ans)))