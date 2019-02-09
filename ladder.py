from math import *
info = input()
h,v = map(int,info.split(" ",1))
degree = (sin(radians(v)))
ans = ceil(h/degree)
print(ans)
