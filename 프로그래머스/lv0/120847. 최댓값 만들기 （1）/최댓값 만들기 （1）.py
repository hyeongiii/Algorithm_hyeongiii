def solution(numbers):
    a = max(numbers)
    numbers.remove(a)
    b = max(numbers)
    answer = a *b
    return answer