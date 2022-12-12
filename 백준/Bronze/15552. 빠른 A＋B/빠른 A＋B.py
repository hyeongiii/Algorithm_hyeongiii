import sys

a = int(sys.stdin.readline().rstrip())

for x in range(a):
    b, c = map(int, sys.stdin.readline().rstrip().split())
    print(b + c)