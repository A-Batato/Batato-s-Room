import random
n = int(input())
m = int(input())

print(1 if ((n % m == 0) or (m % n == 0)) else (random.randint(2, 100)))