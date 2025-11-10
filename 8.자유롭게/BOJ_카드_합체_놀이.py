import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))

for i in range(m):
    cards.sort()
    cards[0] = cards[0] + cards[1]
    cards[1] = cards[0]

print(sum(cards))