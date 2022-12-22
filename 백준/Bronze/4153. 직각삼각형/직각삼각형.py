import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().rstrip().split()))
    if sum(data) == 0:
        break
    M = max(data)
    sum_ = 0

    for i in range(len(data)):
        if data[i] != M:
            m = data[i]**2
            sum_ += m
    if sum_ == M**2 and data[0] != 0:
        print('right')
    elif sum_ != M**2 and data[0] != 0:
        print('wrong')