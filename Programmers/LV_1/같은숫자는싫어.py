def solution(arr):
    res = [arr[0]]
    for i in arr[1:]:
        if i != res[-1]:
            res.append(i)
        else:
            pass
    return res
