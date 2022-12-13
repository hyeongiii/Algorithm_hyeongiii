import sys

li = []
for i in range(1, 10):
    i = int(sys.stdin.readline().rstrip())
    li.append(i)

for i in range(0, 8):
    for j in range(i+1, 9):
        new = sorted(li)
        del new[j]
        del new[i]
        result = sum(new)
        if result == 100:
            break
    if result == 100:
        break

for x in new:
    print(x)