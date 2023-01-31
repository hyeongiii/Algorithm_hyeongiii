'''
# 시간 초과
def solution(ingredient):
    answer = 0
    str_in = [str(i) for i in ingredient]
    tmp = ''
    
    for i in str_in:
        tmp += i
        
        if "1231" in tmp:
            answer += 1
            tmp = tmp.replace("1231", "")
        
    return answer
'''

def solution(ingredient):
    answer = 0
    
    s = []
    
    for i in ingredient:
        s.append(i)
        
        if s[-4:] == [1, 2, 3, 1]:
            answer += 1
            
            # 햄버거 포장 (재료 제거)
            for j in range(4):
                s.pop()
    
    return answer