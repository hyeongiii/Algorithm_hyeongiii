'''
내가 푼 풀이
def solution(number):
    answer = 0
    
    for i in range(0, len(number)):
        for j in range(i + 1, len(number)):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer
'''

def solution(number):
    from itertools import combinations    # 조합을 구해주는 함수 사용: combinations
    cnt = 0
    
    for i in combinations(number, 3):
        if sum(i) == 0:
            cnt += 1
            
    return cnt