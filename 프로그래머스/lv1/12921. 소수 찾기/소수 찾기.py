def solution(n):
    num = set(range(2, n + 1))
    
    # 에라토스테네스의 체 알고리즘 (1부터 n까지의 자연수 중 소수 몽땅 구하기)
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(i * 2, n + 1, i))    # i는 소수, i * 2 부터 n+ 1 범위 내의 i 배수를 제거
    

    return len(num)
