def solution(dart):
    tf = list(map(lambda x:x.isdigit(),dart))+[False]
    point = {'S':1,'D':2,'T':3}
    
    round = []
    for idx, i in enumerate(dart):
        if i.isdigit():
            cnt = int(i)
            if tf[idx-1]:
                cnt = 10
        elif i in point:
            if tf[idx+1] or idx==(len(dart)-1):
                round.append([cnt,cnt**point[i]])
                cnt = ''
            else:
                cnt **=point[i]
        else:
            if i == '*':
                if len(round) != 0:
                    round[-1][1] *= 2
                round.append([cnt,cnt*2])
            else:
                round.append([cnt,cnt*-1])
                
    return sum([i[1] for i in round])
