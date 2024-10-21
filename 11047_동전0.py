import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]

coin.sort(reverse=True)

total = 0

while K > 0:
    for co in coin:
        if K // co > 0:
            total += K // co
            K = K % co
print(total)
