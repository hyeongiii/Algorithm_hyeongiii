def solution(a, b):
    # 답을 반환할 변수 초기화
    answer = 0
    
    # 배열의 길이(0, n-1) 만큼 반복하여 a[i] * b[i] 값을 더해간다.
    for i in range(len(a)):
        answer += a[i] * b[i]
        
    return answer