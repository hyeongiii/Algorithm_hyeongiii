'''
내가 푼 풀이
def solution(s):
    answer = ""
    tmp = ""
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4",
           "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}    # 딕셔너리 선언
    
    for i in s:
        if i.isnumeric():    # i가 숫자형태일 경우, 바로 answer에 더해준다.
            answer += i
        else:    # i가 숫자형태가 아닐 경우, tmp에 저장해가면서 tmp가 딕셔너리 키가 될 때 키에 대한 값을 answer에 더해준다.
            tmp += i
            if tmp in dic.keys():
                answer += dic[tmp]
                tmp = ""
                
    return int(answer)
'''

def solution(s):
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4",
           "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = s
    
    for key, value in dic.items():
        answer = answer.replace(key, value)
    
    return int(answer)