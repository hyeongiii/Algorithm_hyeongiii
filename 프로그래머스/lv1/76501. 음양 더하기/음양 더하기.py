def solution(absolutes, signs):
    answer = 0
    li = []
    
    for i in range(len(signs)):
        if signs[i] == True:
            li.append(absolutes[i])
        else:
            li.append(-absolutes[i])
            
    answer = sum(li)        
    return answer