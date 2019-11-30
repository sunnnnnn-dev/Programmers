def solution(num, lost, reserve):
    res = num - len(lost)
    cnt = 0
    
    a = list(set(lost).intersection(reserve))
    for i in a:
        reserve.remove(i)
        lost.remove(i)
        cnt += 1
    
    for i in lost: 
        if i-1 in reserve:
            reserve.remove(i-1)
            cnt += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            cnt +=1
            
    return cnt+res
