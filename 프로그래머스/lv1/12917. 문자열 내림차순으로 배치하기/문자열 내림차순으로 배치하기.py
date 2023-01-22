def solution(s):
    li = list(s)    # str -> list
    li.sort(reverse = True)        # list를 역순으로 정렬
    
    return "".join(li)