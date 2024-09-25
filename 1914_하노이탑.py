#%%
n = int(input())
  
def hanoi(n, s, e):
  if n == 1:
    print(s, e)
    return
  else:
    hanoi(n -1, s, 6-s-e)
    print(s, e)
    hanoi(n-1, 6-s-e, e)

print(2**n -1)
if n <= 20:
  hanoi(n, 1, 3)
















