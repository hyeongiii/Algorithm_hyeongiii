def solution(order):
    tsn = '369'
    answer = 0
    for i in str(order):
        if i in tsn:
            answer += 1
    return answer