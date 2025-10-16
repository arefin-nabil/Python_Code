from functools import reduce

n = int(input())
lst = input().split()
lst2 = input().split()

lst = [int(x) for x in lst]
lst2 = [int(x) for x in lst2]

lst3 = lst2+lst

for i in lst3:
    print(i, end=" ")
# print(lst3)
