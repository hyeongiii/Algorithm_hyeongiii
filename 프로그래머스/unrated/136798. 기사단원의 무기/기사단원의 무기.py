def divisor(n):
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        a=divisor(i)
        if a>limit:
            answer+=power
        else:
            answer+=a
        
    return answer