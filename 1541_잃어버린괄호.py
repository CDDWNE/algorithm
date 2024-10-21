import sys
input = sys.stdin.readline

first = input().split('-')
result = []


for i in first:
    hap = 0
    li = i.split('+')

    for j in li:
        hap += int(j)
    result.append(hap)

ans = result[0]

for k in range(1, len(result)):
    ans -= result[k]
print(ans)