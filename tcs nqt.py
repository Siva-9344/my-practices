n = int(input())
j = 0
k = [0 for i in range (n)]

for i in range (n):
    a = int(input())
    if a!= 0:
        k[j] = a
        j += 1

for i in k:
    print(i,end ="")
