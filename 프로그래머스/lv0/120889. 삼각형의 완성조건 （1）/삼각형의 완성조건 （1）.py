def solution(sides):
    if sum(sides) - max(sides) > max(sides):
        answer = 1
    else:
        answer = 2
    return answer