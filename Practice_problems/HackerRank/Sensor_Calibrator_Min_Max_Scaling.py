# formula: norm = (x - min_v) / (max_v - min_v)


x, min, max = input().split()
x = float(x)
min = float(min)
max = float(max)

norm = (x - min) / (max - min)

print(f"{norm:.2f}")
