import sys
input = sys.stdin.readline

num = int(input().rstrip())
li = []

for _ in range(num):
    li.append(list(map(str, input().rstrip().split())))

li.sort(key=lambda x : int(x[0]))

for i in li:
    print(i[0], i[1])