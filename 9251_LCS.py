import sys
input = sys.stdin.readline

first = list(input().strip())
second = list(input().strip())

lcs = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1] == second[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(max(map(max, lcs)))