def solution(s):
    num = "0123456789"
    if len(s) != 4 and len(s) != 6:
        return False
    else:
        for i in s:
            if not i in num:
                return False
        return True