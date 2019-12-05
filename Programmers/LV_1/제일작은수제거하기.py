def solution(arr):
    num = min(arr)
    arr.remove(num)
    return arr if arr else [-1]
