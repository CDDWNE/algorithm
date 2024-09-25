#%%

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

def solution(arr):
    if len(arr) == 0:
        return
    
    mid = arr[0]
    tempL, tempR = [], []
    for i in range(1, len(arr)):
        if arr[i] > mid:
            tempL = arr[1:i]
            tempR = arr[i:]
            break
    else:
        tempL = arr[1:]
    solution(tempL)
    solution(tempR)
    print(mid)

solution(arr)