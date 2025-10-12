n, m = input().split()
ar = input().split()
A = input().split()
B = input().split()

A=set(A)
B=set(B)

hpy = 0

for i in ar:
    if i in A:
        hpy+=1
    if i in B:
        hpy-=1

print(hpy)

