def solution(s):
    li = list(map(str, s.rstrip().split()))
    
    answer = 0
    pre = int(li[0])
    for i in li:
        if i == 'Z':
            answer -= pre
        else:
            answer += int(i)
            pre = int(i)
    return answer         