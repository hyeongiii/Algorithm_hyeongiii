def solution(word):
    answer = True
    cnt_p = 0
    cnt_y = 0
    word = word.lower()
    
    for i in word:
        if i == "p":
            cnt_p += 1
        elif i == "y":
            cnt_y += 1
    
    if cnt_p != cnt_y:
        answer = False

    return answer