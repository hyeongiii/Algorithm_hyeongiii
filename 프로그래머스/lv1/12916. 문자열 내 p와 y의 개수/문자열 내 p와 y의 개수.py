def solution(s):
    answer = True
    pc = 0
    yc = 0
    word = s.upper()
    for i in word:
        if i == "P":
            pc += 1
        elif i == "Y":
            yc += 1
    
    if pc != yc:
        answer = False
    
    return answer