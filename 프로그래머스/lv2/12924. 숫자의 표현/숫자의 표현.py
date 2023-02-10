def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        sum_ = 0
        for j in range(i, n + 1):
            sum_ += j
            if sum_ == n:
                answer += 1
            elif sum_ > n:
                break
            
    return answer