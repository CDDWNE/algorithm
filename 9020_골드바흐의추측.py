#%%

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    num = int(input())
    a, b = num//2, num//2
    
    for _ in range(num//2):
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
# %%

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for i in range(int(input())):
    n = int(input())
    a = n // 2
    b = n // 2
    for j in range(n // 2):
        if is_prime(a) and is_prime(b):
            print(a, b)
        else:
            a -= 1
            b += 1