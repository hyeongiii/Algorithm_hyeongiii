def solution(hp):
    answer = 0
    
    
    a = hp // 5
    
    hp -= a * 5
    
    b = hp // 3
    
    hp -= b * 3
    
    c = hp
    
    answer = a+b+c
        
    
    return answer