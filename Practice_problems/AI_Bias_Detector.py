inp = input().split()

a = 0
b = 0

for i in inp:
    if i == "A":
        a += 1
    if i == "B":
        b += 1

p_a = (a * 100) / len(inp)
p_b = (b * 100) / len(inp)

if p_a > 70 or p_b > 70:
    print("Biased Model")
else:
    print("Fair Model")
