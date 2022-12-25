def solution(rsp):
    rsp_dic = {"2":"0", "0":"5", "5":"2"}
    answer = ''
    
    for i in rsp:
        answer += rsp_dic[i]
        
    return answer