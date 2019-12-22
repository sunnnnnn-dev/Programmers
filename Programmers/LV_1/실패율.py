def solution(n,stages):
    res = []
    cnt = len(stages)
    for i in range(1,n+1):
        res.append([i,stages.count(i),cnt])
        cnt -= stages.count(i)
        
    res2 = []
    for j in res:
        if j[2] == 0:
            res2.append([j[0],0])
        else:
            res2.append([j[0],j[1]/j[2]])
    
    res2.sort(key=lambda x:x[1],reverse=True)
    return [i[0] for i in res2]
