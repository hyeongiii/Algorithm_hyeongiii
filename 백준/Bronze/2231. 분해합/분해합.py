import sys

num = int(sys.stdin.readline().rstrip())

for x in range(num+1):
    nums = list(map(int, str(x)))
    sum_ = x + sum(nums)
    if sum_ == num:
        print(x)
        break
    if num == x:
        print(0)