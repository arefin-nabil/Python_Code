n = input()

num = input().split()

num = [int(x) for x in num]

mn = min(num)

idx = num.index(min(num))

print(mn, idx+1)
