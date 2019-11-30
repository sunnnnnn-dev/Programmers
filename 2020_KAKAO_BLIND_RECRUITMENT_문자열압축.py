def solution(sam):
    
    if len(sam) < 1 or len(sam) > 1000:
        return 's의 길이는 1 이상 1,000 이하입니다.'
    
    r_res=[]   
    for i in range(1,len(sam)+2):
        cnt = 1
        res = 0
        for j in range(0,len(sam),i):
            if sam[j:j+i] == sam[j+i:j+(2*i)]:
                cnt += 1
            else:
                if cnt > 1:
                    res += len(str(cnt))+i
                    cnt = 1
                else:
                    res += len(sam[j:j+i])
            
        r_res.append(res)
    return min(r_res)