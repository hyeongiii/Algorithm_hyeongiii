def solution(N, stages):
    tmp = {}
    num = len(stages)
    
    for i in range(1, N + 1):
        if num != 0:
            tmp[i] = stages.count(i) / num
            num -= stages.count(i)
        else:
            tmp[i] = 0
    
    return sorted(tmp, key=lambda x : tmp[x], reverse = True)