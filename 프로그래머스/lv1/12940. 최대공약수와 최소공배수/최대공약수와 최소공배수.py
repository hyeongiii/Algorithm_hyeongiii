def solution(n, m):
    a, b = max(n, m), min(n, m)
    t = 1
    
    while t > 0:
        t = a % b
        a, b = b, t
    answer = [a, n*m//a]
    
    return answer