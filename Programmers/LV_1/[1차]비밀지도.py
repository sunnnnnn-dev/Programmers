def solution(n,arr1,arr2):
    res = []
    for a1,a2 in zip(arr1,arr2):
        res_str = ''
        for i in range(n-1,-1,-1):
            str_1 = ''
            str_2 = ''
            
            if 2**i <= a1:
                str_1 = '#'
                a1 -= 2**i
            else:
                str_1 = ' '
            if 2**i <= a2:
                str_2 = '#'
                a2 -= 2**i
            else:
                str_2 = ' '
                
            if str_1 == ' ' and str_2 == ' ':
                res_str += ' '
            else:
                res_str += '#'
        res.append(res_str)
    return res
