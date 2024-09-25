#%%
import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]

def sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    new = []
    i = 0
    j = 0
    while len(left) > i and len(right) > j:
        if left[i] > right[j]:
            new.append(right[j])
            j += 1
        else:
            new.append(left[i])
            i += 1
    while j < len(right):
        new.append(right[j])
        j += 1
    while i < len(left):
        new.append(left[i])
        i += 1
    return new

for x in sort(li):
    print(x)
    
