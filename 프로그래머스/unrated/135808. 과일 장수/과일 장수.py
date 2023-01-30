def solution(k, m, score):
    answer = 0
    
    score.sort(reverse = True)
    a = len(score) // m
    
    for i in range(a):
        tmp = score[i*m:i*m+m]
        price = min(tmp)
        answer += price * m

    return answer