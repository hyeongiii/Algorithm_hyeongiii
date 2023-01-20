def solution(a, b):
    '''
    내가 푼 풀이
    
    answer = 0
    hi = max(a, b)
    lo = min(a, b)
    
    for i in range(lo, hi + 1):
        answer += i
        
    return answer
    
    '''
    
    if a > b:
        a , b = b, a
    if a == b:
        return a
    return sum(range(a, b + 1))
