def solution(s):
    try:
        int(s)
        if len(s) == 6 or len(s) == 4:
            return True
    except:
        return False
    else:
        return False
