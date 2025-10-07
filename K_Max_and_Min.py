a,b,c = input().split()
a= int(a)
b=int(b)
c=int(c)

min =a
max =a

if b<min:
    min =b
if c<min:
    min =c

if b>max:
    max=b
if c>max:
    max=c


print(min,max)

