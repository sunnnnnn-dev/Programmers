def solution(n, m):
    res = [i for i in range(1,n+1) if n%i==0 and m%i==0]
    return [max(res),(n//max(res))*m]
