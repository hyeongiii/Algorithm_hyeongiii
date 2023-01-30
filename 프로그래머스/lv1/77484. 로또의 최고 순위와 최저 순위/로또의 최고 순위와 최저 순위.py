def solution(lottos, win_nums):
    answer = []
    
    num = lottos.count(0)
    win = list(set(lottos) & set(win_nums))
    maxi = len(win) + num
    mini = len(win)
    
    rank = [6, 6, 5, 4, 3, 2, 1]
    for i in (maxi, mini):
        answer.append(rank[i])
    
    return answer