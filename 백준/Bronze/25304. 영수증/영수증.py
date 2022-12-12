import sys

total = int(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline().rstrip())
sum = 0

for i in range(num):
    price, count = map(int, sys.stdin.readline().rstrip().split())
    sum += price * count
    
if total == sum:
    print('Yes')
else:
    print('No')