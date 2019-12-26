def solution(arr):
    arr = arr.replace('()','8')
    cnt = 0
    bar = 0
    for i in arr:
        if i == '(':
            bar += 1
        elif i == '8':
            cnt += 1*bar
        else:
            bar -= 1
            cnt += 1
    return cnt
