def solution(a,b):
    ab = [sum([i for i in range(a,b-1,-1)]), sum([i for i in range(a,b+1)])]
    return ab[0] if ab[0] !=0 else ab[1]
