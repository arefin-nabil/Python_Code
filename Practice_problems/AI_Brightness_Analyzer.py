bright = input().split()

bright2=[int(x) for x in bright]

sum = 0
for i in bright2:
    sum = sum+i

avg = sum/len(bright2)


if avg < 85:
    print("Dark Image")
elif avg >= 85 and avg <= 170:
    print("Normal Image")
elif avg>170:
    print("Bright Image")
# print(bright2)


# If the average brightness  → print
# If  average brightness  → print
# If average brightness > 170 → print
