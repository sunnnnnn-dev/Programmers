def solution(x, n):
    return [j+i*x for i,j in enumerate([x]*n)]
