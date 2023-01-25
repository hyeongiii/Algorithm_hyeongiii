# hash 활용
def solution(participant, completion):
    answer = ''
    sumHash = 0
    dic = {}

    for part in participant:
        dic[hash(part)] = part
        sumHash += int(hash(part))

    for com in completion:
        sumHash -= hash(com)
        
    answer = dic[sumHash]
    
    return answer

'''
HashMap : key-value 짝을 이뤄 관리하는 클래스로, 이 문제에서 key는 hash한 값이고 value는 각 선수의 이름이다.
HashMap에 각 이름의 hash값을 구하고 'hashing'한 값을 모두 더한 것이 sumHash가 된다.

completion을 순회하며 각 이름들의 hash 값을 빼주면, 결국 완주하지 않은 선수의 hash 값만 남게 된다.
그 때, HashMap에서 해당 해시값을 key로 가진 이름을 반환하면 답이다.
'''