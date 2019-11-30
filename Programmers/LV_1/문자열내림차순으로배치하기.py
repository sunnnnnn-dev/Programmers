def solution(s):
    res = [i for i in s.encode()]
    res.sort(reverse=True)

    res2 = ''
    for i in res:
        res2 += chr(i)

    return res2
