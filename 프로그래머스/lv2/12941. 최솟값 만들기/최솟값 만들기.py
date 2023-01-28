'''
내가 푼 풀이 : 효율성 테스트 모두 실패

def solution(A,B):
    answer = 0

    for i in range(len(A)):
        a1, a2 = max(A), min(A)
        b1, b2 = max(B), min(B)
        
        if a1 * b2 >= a2 * b1:
            answer += a2 * b1
            A.remove(a2)
            B.remove(b1)
        else:
            answer += a1 * b2
            A.remove(a1)
            B.remove(b2)

    return answer
'''

def solution(A, B):
    answer = 0
    
    # A는 정방향 B는 역방향으로 정렬
    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)):
            answer += A[0] * B[0]
            A.pop(0)
            B.pop(0)
            
    return answer