def solution(lottos, win_nums):
    answer = []
    
    num = lottos.count(0)
    win = list(set(lottos) & set(win_nums))
    maxi = len(win) + num
    mini = len(win)
    
    for i in (maxi, mini):
        if i == 6:
            answer.append(1)
        elif i == 5:
            answer.append(2)
        elif i == 4:
            answer.append(3)
        elif i == 3:
            answer.append(4)
        elif i == 2:
            answer.append(5)
        else:
            answer.append(6)
    
    return answer