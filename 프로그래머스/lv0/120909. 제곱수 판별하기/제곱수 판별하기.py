def solution(n):
    sq = (n **(1/2))
    if sq % 1 == 0:
        answer = 1
    else:    
        answer = 2
    return answer