def solution(d, budget):
    d.sort()
    
    s = 0    # 예산 합계
    count = 0    # 지원할 수 있는 부서의 개수
    
    for i in d:
        if s + i <= budget:
            count += 1
            s += i
        else:
            break
    return count