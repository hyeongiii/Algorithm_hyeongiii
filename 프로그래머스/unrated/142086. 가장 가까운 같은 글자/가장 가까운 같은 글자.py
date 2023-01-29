def solution(s):
    answer = []
    dic = {}
    
    for i in range(len(s)):
        if dic.get(s[i]) == None:
            dic[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
            dic[s[i]] = i
            
    return answer