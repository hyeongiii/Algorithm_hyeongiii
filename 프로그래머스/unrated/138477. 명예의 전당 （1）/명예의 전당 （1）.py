def solution(k, score):
    answer = []
    tmp = []
    
    for i in score:
        tmp.append(i)
        if len(tmp) > k:
            tmp.remove(min(tmp))
        answer.append(min(tmp))
        
    return answer