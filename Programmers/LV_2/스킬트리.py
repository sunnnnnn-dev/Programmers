def solution(skill, skill_trees):
    res = [[] for i in range(len(skill_trees))]
    for alpha in skill:
        for idx, string in enumerate(skill_trees):
            if alpha in string:
                res[idx].append(string.index(alpha))
            else:
                res[idx].append(27)
        
    cnt = 0
    for i in res:
        j = i[:]
        i.sort()
        if i == j:
            cnt += 1
    return cnt
