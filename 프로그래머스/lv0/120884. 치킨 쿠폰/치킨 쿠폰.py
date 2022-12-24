def solution(chicken):
    answer = 0
    
    while chicken >= 10:
        service = chicken // 10
        chicken = service + chicken % 10
        answer += service
    return answer