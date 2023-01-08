def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    else:
        if not s.isdecimal():
            answer = False
    return answer