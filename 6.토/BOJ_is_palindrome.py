import sys
nums = sys.stdin.readlines()

def is_palindrome(num):
    length = len(num)
    for i in range(length // 2):
        if num[i] != num[length - 2 - i]:
            return False
    return True

for n in nums[:-1]:
    print("yes" if is_palindrome(n) else "no")