def solution(price, money, count):
    tmp = 0
    
    for i in range(1, count + 1):
        tmp += i * price
    
    if tmp - money <= 0:
        return 0

    return tmp - money