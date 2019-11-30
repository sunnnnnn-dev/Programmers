def solution(s, num):
    return sorted(sorted(s),key=lambda x:x[num])
