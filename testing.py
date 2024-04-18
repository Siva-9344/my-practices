import math
n=int(input())
k=(1<< int(math.log2(n))+1)-1
print(n^k)


n = 10
b  = bin(n)
print(b)
