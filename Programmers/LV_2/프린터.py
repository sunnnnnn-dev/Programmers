def solution(pri,location):
    cnt = 1
    while pri: 
        idx = pri.index(max(pri)) # max의 위치
        if location == idx:
            break

        pri = pri[idx+1:] + pri[:idx]
        if location < idx:
            location += len(pri[idx:])
            cnt += 1
        else:
            location -= len(pri[:idx+1])
            cnt += 1
    return cnt
