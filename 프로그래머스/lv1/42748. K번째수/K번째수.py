def solution(array, commands):
    answer = []
    li = []
    
    for x in commands:
        i = x[0]
        j = x[1]
        k = x[2]
        li = array[i-1:j]
        li.sort()
        answer.append(li[k-1])
    return answer