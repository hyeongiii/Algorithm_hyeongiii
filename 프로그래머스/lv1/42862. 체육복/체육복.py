def solution(n, lost, reserve):
    answer = 0
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난 당한 경우 고려
    reserve_unique = [r for r in reserve if r not in lost]
    lost_unique = [l for l in lost if l not in reserve]
    
    reserve_unique.sort()
    
    for i in reserve_unique:
        if i - 1 in lost_unique:
            lost_unique.remove(i - 1)
        elif i + 1 in lost_unique:
            lost_unique.remove(i + 1)
            
    return n - len(lost_unique)