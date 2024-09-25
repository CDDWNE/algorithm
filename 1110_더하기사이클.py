#%%
# import sys
# input = sys.stdin.readline

# n = input()
# new_num = []
# if int(n) < 10:
#     new_num.append('0')
#     new_num.append(n)
# else:
#     new_num.append(n[1])
#     new_num.append(str(int(n[0])+ int(n[1]))[-1])

# count = 0

# while new_num[0] + new_num[1] != n:
#     new_num[0] = new_num[1]
#     new_num[1] = str(int(n[0]) + int(n[1]))[-1]
#     count += 1

# print(count)

n = int(input())
count = 0
temp = n
while True:
    ten = temp // 10
    one = temp % 10
    hap = ten + one
    temp = int(str(one) + str(hap)[-1])
    count += 1
    if temp == n:
        print(count)
        break
    else:
        continue