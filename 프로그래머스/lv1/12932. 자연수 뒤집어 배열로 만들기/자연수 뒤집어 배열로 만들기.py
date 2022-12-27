def solution(n):
    num = str(n)
    reverse = num[::-1]
    li = list(reverse)
    answer = []
    
    for i in li:
        answer.append(int(i))
    
    return answer