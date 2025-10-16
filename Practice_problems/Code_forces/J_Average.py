from functools import reduce

n = int(input())
lst = input().split()
lst2 = [float(l) for l in lst]

sm = reduce(lambda x, y : x+y, lst2)

avg = sm/n

print(f"{avg:.7f}")
