t = int(input())

inp = input()

nums = inp.split()

pos = 0
neg = 0
evn = 0
odd = 0

for i in range(t):
    x = int(nums[i])

    if x > 0:
        pos+=1
    elif x<0:
        neg+=1
    
    if x%2==0:
        evn+=1
    elif x%2!=0:
        odd+=1


print("Even:", evn)
print("Odd:", odd)
print("Positive:", pos)
print("Negative:", neg)

