def solution(bin1, bin2):
    
    sum = bin(int(bin1, 2) + int(bin2, 2))
    answer = sum[2:]
    return answer