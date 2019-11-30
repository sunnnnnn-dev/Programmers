def solution(a,b):
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    months = [5,1,2,5,0,3,5,1,4,6,2,4]
    num = months[a-1]
    return day[(b+num)%7-1]
