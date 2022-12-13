import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
li = list(map(int, sys.stdin.readline().rstrip().split()))

arr = []

for i in li:
    if i < x:
        arr.append(i)

result = ' '.join(str(n) for n in arr)
print(result)