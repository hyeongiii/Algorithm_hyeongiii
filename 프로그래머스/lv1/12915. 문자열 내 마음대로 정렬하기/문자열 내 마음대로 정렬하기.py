def solution(strings, n):
    
    return sorted(strings, key = lambda x : (x[n], x))

# sorted(iterator, key = ~ ) : ~을 기준으로 정렬
# lambda x : (x[n], x) -> 조건이 여러개일 때, 튜플 내의 순으로 조건의 우선순위를 정할 수 있다.