t = int(input())

lst = input().split()

lst = [int(i) for i in lst]

mn = min(lst)
mx = max(lst)

mni = lst.index(mn)
mxi = lst.index(mx)

lst[mni] = mx
lst[mxi] = mn

for i in lst:
    print(i, end=" ")
