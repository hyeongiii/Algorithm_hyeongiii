def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        if cnt(i) % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer

# 약수의 개수 구하는 함수
def cnt(num):
    cnt = 1
    
    for i in range(1, num//2 + 1):
        if num % i == 0:
            cnt += 1
            
    return cnt