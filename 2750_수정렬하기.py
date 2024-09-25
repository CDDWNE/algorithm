#%%
N = int(input())
li = []
for i in range(N):
    num = int(input())
    li.append(num)
    
li.sort()
for x in li:
    print(x)