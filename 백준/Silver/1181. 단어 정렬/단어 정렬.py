import sys
input = sys.stdin.readline

num = int(input().rstrip())
li = []
for _ in range(num):
    li.append(input().rstrip())

new_li = list(set(li))
new_li.sort()
new_li.sort(key=len)

for x in new_li:
    print(x)