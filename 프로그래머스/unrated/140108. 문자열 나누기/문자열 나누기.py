def solution(s):
    answer = 0
    
    while s:
        c = s[0]
        
        c_cnt = 1
        x_cnt = 0
        idx = 0
        
        for i in range(1, len(s)):
            if c_cnt == x_cnt:
                break
                
            idx = i
            if s[i] == c:
                c_cnt += 1
            else:
                x_cnt += 1
        
        answer += 1
        
        if len(s) - 1 == idx:
            s = ''
        else:
            s = s[idx + 1:]
            
    return answer