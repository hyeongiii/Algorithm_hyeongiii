def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    l = len(answers)
    # 수포자 1, 2, 3의 답안
    a1 = s1 * (l // 5) + s1[:(l % 5)]
    a2 = s2 * (l // 8) + s2[:(l % 8)]
    a3 = s3 * (l // 10) + s3[:(l % 10)]
        
    cnt1, cnt2, cnt3 = 0, 0, 0
    
    # 수포자 1, 2, 3의 답안과 답을 비교한 뒤, 맞았을 경우 cnt 를 1 증가
    for i in range(l):
        if answers[i] == a1[i]:
            cnt1 += 1
        if answers[i] == a2[i]:
            cnt2 += 1
        if answers[i] == a3[i]:
            cnt3 += 1
    
    # cnt 값중 최대값을 구한뒤, 각각의 cnt 가 m 과 같을 경우 answer에 추가
    m = max(cnt1, cnt2, cnt3)
    
    if m == cnt1:
        answer.append(1)
    if m == cnt2:
        answer.append(2)
    if m == cnt3:
        answer.append(3)
    
    return answer