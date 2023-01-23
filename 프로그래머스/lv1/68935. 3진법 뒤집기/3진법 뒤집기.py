def solution(n):
    answer, tmp = 0, ""
    
    while n > 0:
        # 3진법의 역순으로 저장됨
        tmp += str(n % 3)
        n //= 3
    
    # 계산을 위해 [3진법 역순] -> [3진법]
    tmp = tmp[::-1]
    
    # 3진법 -> 10진법
    for i in range(1, len(tmp)):
        answer += int(tmp[i]) * (3 ** i)
    
    return answer + int(tmp[0])
    