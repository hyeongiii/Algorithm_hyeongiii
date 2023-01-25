def solution(numbers):
    answer = []
    
    # 이중 반복문을 사용하여 서로 다른 인덱스의 숫자 합을 모두 구한 뒤, answer에 삽입
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    # answer를 집합 형태(set)로 만들어서 중복값을 제거한 뒤, 다시 리스트로 변환하여 오름차순으로 정렬
    answer = list(set(answer))
    answer.sort()
    
    return answer