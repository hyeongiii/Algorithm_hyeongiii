def solution(n):
    li = list(str(n))
    li.reverse()
    
    for i in range(len(li)):
        li[i] = int(li[i])
    
    return li
