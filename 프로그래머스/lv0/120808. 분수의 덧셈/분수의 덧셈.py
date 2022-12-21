import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    
    gcd = math.gcd(denum, num)
    
    answer = []
    answer.append(denum//gcd)
    answer.append(num//gcd)
    return answer