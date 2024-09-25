#%%

nan_list = [int(input()) for _ in range(9)]

hap = sum(nan_list)

for i in range(8):
    for j in range(i + 1, 9):
        if hap - (nan_list[i] + nan_list[j]) == 100:
            x = nan_list[i]
            y = nan_list[j]

nan_list.sort()
for k in nan_list:
    if k == x or k == y:
        pass
    else:
        print(k)
