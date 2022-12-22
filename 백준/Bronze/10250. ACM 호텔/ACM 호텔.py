import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    h, w, n = map(int, input().rstrip().split())

    # 해당 손님이 머물 객실의 위치 구하기
    if n // h < 1:
        width = 1
    elif n % h == 0:
        width = n // h
    else:
        width = n // h + 1

    # 해당 손님이 머물 객실의 층수 구하기    
    if n % h == 0:
        height = h
    else:
        height = n % h

    # 만약, 객실의 위치가 10번대 미만일 경우, 방번호 앞에 0 붙이기
    if width < 10:
        width = '0' + str(width)

    print(str(height) + str(width))