t = int(input())
y=0;n=0
for i in range(t):
    v=input()
    if v=="YES":
        y+=1
    else:
        n+=1
if y>=n:
    print("ACCEPT")
else:
    print("REJECT")