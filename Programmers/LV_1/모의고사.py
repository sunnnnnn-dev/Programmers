def solution(answers):
    
    long = len(answers)
    if long > 10000:
        return '시험은 최대 10,000 문제 입니다.'
        
    num_1 = [1,2,3,4,5]
    num_2 = [2,1,2,3,2,4,2,5]
    num_3 = [3,3,1,1,2,2,4,4,5,5]
    
    res_1 = num_1*int(long//5) + num_1[:long%5]
    res_2 = num_2*int(long//8) + num_2[:long%8]
    res_3 = num_3*int(long//10) + num_3[:long%10]
    
    res = {1:0,2:0,3:0}
    for a,b in enumerate(answers):
        if res_1[a] == b:
            res[1] += 1
        if res_2[a] == b:
            res[2] += 1
        if res_3[a] == b:
            res[3] += 1
        if b > 5:
            return '문제의 정답은 1,2,3,4,5 중 하나입니다.'
        
    max_res = max(res.values())
    d_res = [i[0] for i in res.items() if i[1]==max_res]
    return d_res
