def solution(n):
    a = '수';b = '박'
    res = ''
    for i in range(n):
        if (i+1)%2 == 1:
            res += a
        else:
            res += b
    return res
