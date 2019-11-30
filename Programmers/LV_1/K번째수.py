def solution(array, commands):
    res = []
    for i in commands:
        list1 = array[i[0]-1:i[1]]
        list1.sort()
        res.append(list1[i[2]-1])
    return res
