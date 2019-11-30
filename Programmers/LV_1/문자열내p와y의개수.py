def solution(s):
    cnt_p = s.lower().count('p')
    cnt_y = s.lower().count('y')
    return cnt_p == cnt_y
