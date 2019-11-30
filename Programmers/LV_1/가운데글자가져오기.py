def solution(s):
    long = len(s)
    return s[int(long/2)-1+long%2:int(long/2)+1]
