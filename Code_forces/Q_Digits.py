x = int(input())

for i in range(x):
    n = int(input())
    if n == 0:
        print("0", end=" ")
    while n>0:
        m = n%10
        print(m, end=" ")
        n = n//10
    print()