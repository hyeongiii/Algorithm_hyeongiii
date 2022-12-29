def solution(numbers):
    answer = -1
    li = [0,1,2,3,4,5,6,7,8,9]
    
    for i in numbers:
        if i in li:
            li.remove(i)
    
    answer = sum(li)
    
    return answer