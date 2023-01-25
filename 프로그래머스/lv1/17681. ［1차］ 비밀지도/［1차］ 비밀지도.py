def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        val = bin(i|j)[2:]    # bin(): 10진법 -> 2진법 변환, 앞에 0b가 붙는다.
        val = val.rjust(n, '0')    # rjust(n, 대체 문자): 오른쪽 정렬 후, 글자수가 n보다 작으면 빈자리에 대체 문자를 넣음
        val = val.replace('1', '#')    # replace(기존문자열, 바꿀문자열)
        val = val.replace('0', ' ')
        answer.append(val)
    
    return answer
    
    
    '''
    내가 푼 풀이
    
    for i in range(len(arr1)):
    tmp1 = format(arr1[i], 'b')
    tmp2 = format(arr2[i], 'b')
    part = str(int(tmp1) + int(tmp2))
    string = ''

    if len(part) < n:
        part = "0" * (n - len(part)) + part

    for i in part:
        if i == '0':
            string += ' '
        else:
            string += '#'

    answer.append(string)
    '''