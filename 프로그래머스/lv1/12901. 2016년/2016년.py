def solution(a, b):
    tmp = 0
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for i in range(a):
        tmp += month[i]    # 이전 달까지의 날짜 계산
        
    tmp += b    # 현재 날짜 더하기
    
    return day[tmp % 7]