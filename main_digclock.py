from math import floor
n=int(input())
print(f"{n//3600%24}:{n//60%60:02}:{n%60:02}")