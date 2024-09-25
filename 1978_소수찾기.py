#%%
n = int(input())

arr = list(map(int, input().split()))

def sieve(n):
  isprime = [True] * (n+1)
  isprime[0] = isprime[1] = False
  for i in range(2, n):
    if isprime[i]:
      for j in range(i*i, n+1, i):
        isprime[j] = False
  return isprime

isprime = sieve(1000)

result = 0

for x in arr:
  if isprime[x]:
    result += 1

print(result)

def is_prime(num):
  if num == 1:
    return False
  for i in range(2, int(num)):
    if num % i == 0:
      return False
  return True

def count_prime(li):
  prime_count = 0
  for x in li:
    if is_prime(x):
      prime_count += 1
  
  return prime_count

n = int(input())

li = list(map(int, input().split()))

print(count_prime(li))

def sieve(n):
  isprime = [True] * (n+1)
  isprime[0] = isprime[1] = False
  for i in range(2, n+1):
    if isprime[i]:
      for j in range(i*i, n+1, i):
        isprime[j] = False
  return isprime

isprime = sieve(1000)
N = int(input())

arr = list(map(int, input().split()))
cnt = 0
for x in arr:
  if isprime[x]:
    cnt += 1

print(cnt)

def isprime(num):
  if num == 1:
    return False
  for x in range(2, int(num**0.5) + 1):
    if num % x == 0:
      return False
  return True

def count_prime(arr):
  cnt = 0
  for y in arr:
    if isprime(y):
      cnt += 1
  
  return cnt 

N = int(input())
li = list(map(int, input().split()))
      

print(count_prime(li))

n = int(input())
nli = list(map(int, input().split()))

sosu = 0

for num in nli:
  count = 0
  for i in range(2, num+1):
    if num % i == 0:
      count += 1
    else:
      pass
    
  if count == 1:
    sosu += 1

print(sosu)