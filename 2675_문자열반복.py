#%%


T = int(input())



for x in range(T):
  R, S = input().split()
  R = int(R)
  new = ""
  for y in list(S):
    new += y*R
  
  print(new)