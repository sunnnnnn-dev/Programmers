def solution(n):
    for i in range(1,n//2+2):
        if i**2 == n:
            return (i+1)**2
        elif n > i**2 and n < (i+1)**2:
            return -1
        else:
            continue
