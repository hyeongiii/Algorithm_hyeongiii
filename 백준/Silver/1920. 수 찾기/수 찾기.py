_ = int(input())
data1 = set(map(int, input().split()))
_ = int(input())
data2 = list(map(int, input().split()))

for i in data2:
    if i in data1:
        print(1)
    else:
        print(0)