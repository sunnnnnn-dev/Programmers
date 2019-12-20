def solution(progresses,speeds):
    res = list(map(lambda x,y:round(((100-x)/y)+0.49),progresses,speeds))
    num = res[0]
    cnt = 1
    res_list = []
    for i in res[1:]:
        if i <= num:
            cnt += 1
        else:
            res_list.append(cnt)
            num = i
            cnt = 1            
    return res_list+[cnt]
