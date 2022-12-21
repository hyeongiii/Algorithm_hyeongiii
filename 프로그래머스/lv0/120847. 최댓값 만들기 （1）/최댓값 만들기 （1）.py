def solution(numbers):
    a = max(numbers)
    numbers.remove(a)
    b = max(numbers)
    answer = a *b
    return answer

# 다른 사람 풀이
def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]
