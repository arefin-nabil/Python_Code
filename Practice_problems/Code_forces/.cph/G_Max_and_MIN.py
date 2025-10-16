from functools import reduce

n = int(input())
lst = input().split()

lst = [int(x) for x in lst]

mx = reduce(lambda x, y: x if x > y else y, lst)
mn = reduce(lambda x, y: x if x < y else y, lst)

# mx = list(lambda x,y : x>y)

print(mn, mx)
