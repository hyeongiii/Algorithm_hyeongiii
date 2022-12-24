def solution(n):
    li = []
    
    '''
    for i in range(1, n+1):
        if n % i == 0:
            li.append(i)
    '''
    for i in range(1, int(n **(1/2)) + 1):
        if n % i == 0:
            li.append(i)
            # 몫
            k = n // i
            if k != i:
                li.append(k)
            
            
    answer = sum(li)
    
    return answer