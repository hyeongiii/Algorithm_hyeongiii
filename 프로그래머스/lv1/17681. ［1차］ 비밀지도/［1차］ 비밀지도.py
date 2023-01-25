def solution(n, arr1, arr2):
    answer = []
    
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

    return answer