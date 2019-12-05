def solution(s):
    idx = 0
    res = ''
    for i in s:
        if i == ' ':
            res += ' '
            idx = 0
        else:
            if idx%2 == 0:
                res += i.upper()
            else:
                res += i.lower()
            idx += 1
    return res
