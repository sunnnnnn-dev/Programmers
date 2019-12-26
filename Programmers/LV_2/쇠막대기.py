def solution(arr):
    arr = arr.replace('()','8')
    stick = []
    cnt = 0
    for i in arr:
        if i == '(':
            stick.insert(0,i)
        elif i == '8':
            stick.insert(0,i)
        else:
            idx = stick.index('(')
            cnt += stick[:idx].count('8')+1
            del stick[idx]
    return cnt
