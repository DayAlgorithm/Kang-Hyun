import sys
input = sys.stdin.readline
string = input().strip()

length = len(string)
longest = -1

if string[::-1] != string:
    longest = length
elif string == string[0] * length:
    longest = -1
else:
    longest = length - 1

print(longest)