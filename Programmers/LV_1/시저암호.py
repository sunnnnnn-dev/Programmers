def solution(s,n):
    res=''
    for i in s:
        if ord(i) in range(65,91):
            res += chr(65+(ord(i)+n-65)%26)
        elif ord(i) in range(97,123):
            res += chr(97+(ord(i)+n-97)%26)
        else:
            res += i
    return res
