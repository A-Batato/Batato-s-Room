x = int(input())
y = int(input())
z =int(input())

if x > y and z < y:
    print(x)
elif y > z and z > y:
    print(y)
else: print(z)