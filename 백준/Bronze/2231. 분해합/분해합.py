import sys

num = int(sys.stdin.readline())
st = 0

if num > 99:
    st = num - len(str(num)) * 9

N = 0
for i in range(st, num):
    li = list(map(int, str(i)))
    result = i + sum(li)
    if(num == result):
        N = i
        break
print(N)        