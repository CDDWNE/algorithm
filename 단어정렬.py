#%%
import sys
input = sys.stdin.readline

T = int(input())
li = [input().strip() for _ in range(T)]

def compare(x, y):
    if len(x) != len(y):
        return len(y) < len(x)
    else:
        return y < x

def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    left = [x for x in arr if compare(pivot, x)]
    right = [x for x in arr if compare(x, pivot)]
    
    return qsort(left) + [pivot] + qsort(right)

for x in qsort(li):
    print(x)

for x in range(3):
    print(x)