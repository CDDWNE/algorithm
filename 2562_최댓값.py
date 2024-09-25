#%%

_max = -1
idx = -1


for i in range(9):
  n = int(input())
  if _max < n:
    _max = n
    idx = i

print(_max)
print(idx+1)