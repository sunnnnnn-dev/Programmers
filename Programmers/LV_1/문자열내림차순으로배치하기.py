def solution(s):
    res = [i for i in s.encode()]
    res.sort(reverse=True)
    return ''.join(sorted(res,reverse=True))
