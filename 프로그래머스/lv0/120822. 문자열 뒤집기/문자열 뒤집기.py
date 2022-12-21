def solution(my_string):
    answer = ''
    reverse = []
    for i in my_string:
        reverse.append(i)
    
    for _ in range(len(reverse)):
        answer += reverse.pop()
        
    return answer