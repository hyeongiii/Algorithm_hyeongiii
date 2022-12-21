def solution(price):

    if price >= 500000:
        answer = price * 0.8 // 1
    elif price >= 300000:
        answer = price * 0.9 // 1
    elif price >= 100000:
        answer = price * 0.95 // 1
    else:
        answer = price
    return answer

    '''
    다른 사람 풀이
    
    discount_dic = {500000 : 0.8, 300000 : 0.9, 100000 : 0.95, 0 : 1}

    for discount_price, discount_rate in discount_dic.items():
        if price >= discount_price:
            return int(price * discount_rate)
    '''        
