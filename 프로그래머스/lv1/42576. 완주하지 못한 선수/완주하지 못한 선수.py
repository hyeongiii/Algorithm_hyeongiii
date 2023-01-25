def solution(participant, completion):

    # 1. 두 list를 정렬한다.
    participant.sort()
    completion.sort()

    # completion 와 participant를 비교하여 다를 경우, 그 때의 i 값이 완주하지 못한 선수이다.
    for i, j in zip(participant, completion):
        if i != j:
            return i

    # 만약 completion을 다 순회하도록 i와 j가 같다면, 완주하지 못한 선수는 participant의 제일 마지막 인덱스에 있는 값이다.
    return participant[-1]