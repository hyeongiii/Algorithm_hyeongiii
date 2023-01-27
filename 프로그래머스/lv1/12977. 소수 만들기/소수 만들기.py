import itertools

def solution(nums):
    cnt = 0
    
    # itertools.combinations(데이터, n) : 조합 만들기
    for i in itertools.combinations(nums, 3):
        s = sum(i)        
        tmp = 0
        
        # 세 수의 합이 소수인지 판별
        for i in range(2, s//2 + 1):
            if s % i == 0:
                tmp += 1
                break
        
        else:
            cnt += 1

    return cnt