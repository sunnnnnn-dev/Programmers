import math
def solution(n):
    num = int(math.sqrt(n))
    res_list = []
    for i in range(2,num+1):
        for j in range(2,(n//i)+1):
            res_list.append(i*j)
    return n - len(set(res_list)) -1
