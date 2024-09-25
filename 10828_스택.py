#%%
import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        li.append(command[1])
    elif command[0] == 'pop':
        if len(li) > 0:
            pop_num = li.pop() 
            print(pop_num)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(li))
    elif command[0] == 'empty':
        if len(li):
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if len(li):
            print(li[-1])
        else:
            print(-1)