#%%
n = int(input())

row = [0] * n
column = [False] * n

def put(n):
    for i in range(n):
        print(f'{row[i]:2}', end='')
    print()

def queen(x, n):
    for i in range(n):
        if not column[i]:
            row[x] = i
            if x == n:
                put(n)
            else:
                column[i] = True
                queen(x+1, n)
                column[i] = False

queen(0, n)


# %%
