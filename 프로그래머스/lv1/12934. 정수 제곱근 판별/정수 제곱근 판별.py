def solution(n):
    answer = 0
    if (n ** 0.5) % 1 != 0 :
        return -1
    else:
        return ((n ** 0.5) + 1) ** 2