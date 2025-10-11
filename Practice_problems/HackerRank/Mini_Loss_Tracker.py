x = int(input())

t = float(input())

avg = 0
sum = 0

for i in range(x):
    q = float(input())
    sum = sum + q

avg = sum / x

if avg <= t:
    print("PASS")
else:
    print("RETRY")
