import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
seg_tree = [0] * (N * 4)

#배열의 start부터 end까지의 곱을 tree[idx]에 재귀적으로 저장
def init_segtree(start, end, idx): 
    if start == end:
        seg_tree[idx] = arr[start]
        return seg_tree[idx]
    else:
        mid = (start + end) // 2
        seg_tree[idx] = init_segtree(start, mid, 2 * idx) * init_segtree(mid+1, end, 2 * idx + 1) % 1000000007
        return seg_tree[idx]
        
init_segtree(0, N-1, 1)

#   start end : 트리에 저장된 구간, left right : 값을 구하고 싶은 구간, idx는 트리 탐색용
def interval_mul(start, end, idx, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return seg_tree[idx]
    else:
        mid = (start + end) // 2
        return interval_mul(start, mid, 2*idx, left, right) * interval_mul(mid+1, end, 2*idx+1, left, right) % 1000000007

#   start end : 트리 탐색의 구간, idx : 트리 인덱스, target : 바꾸고 싶은 인덱스 번호, changed : 바꿀 수
def set_node(start, end, idx, target, changed):
    if start == target and end == target:
        seg_tree[idx] = changed
        return changed
    if start > target or end < target:
        return seg_tree[idx]
    else:
        mid = (start + end) // 2
        seg_tree[idx] = set_node(start, mid, 2*idx, target, changed) * set_node(mid+1, end, 2*idx+1, target, changed) % 1000000007
        return seg_tree[idx]
        
for i in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        set_node(1, N, 1, b, c)
    elif a== 2:
        print(interval_mul(1, N, 1, b, c))