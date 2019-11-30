def solution(arr):
    res = [arr[0]] + [j for i,j in zip(arr,arr[1:]) if i!= j]
    return res
