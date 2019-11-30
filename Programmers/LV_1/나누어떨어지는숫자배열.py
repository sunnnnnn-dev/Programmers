def solution(arr,divisor):
    res = [ i for i in arr if i%divisor == 0 ]
    res.sort()
    if sum(res) == 0:
        return [-1]
    else:
        return res
