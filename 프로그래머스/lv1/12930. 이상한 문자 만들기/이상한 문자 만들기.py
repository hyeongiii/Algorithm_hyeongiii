def solution(s):
    li = s.split(" ")
    answer = ""

    for i in li:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "
        
    return answer[:-1]