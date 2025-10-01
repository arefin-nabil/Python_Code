# range function
# it is one kind of list data structure
a = list(range(10))
print(a)            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range have three part ----- range(start, end, step)

# for ascending
b = list(range(4, 10))
print(b)            # [4, 5, 6, 7, 8, 9]

c = list(range(0, 10, 2))
print(c)            # [0, 2, 4, 6, 8]


# for descending
d = list(range(10, 0, -1))
print(d)            # [4, 5, 6, 7, 8, 9]



# 1. For Loop
# 2. While Loop
# 3. Nested Loop


# normal for loop
for i in range(10):
    print(i, "Nabil")

# Using String in for loop
s = "Hi, I am Nabil"
for letter in s:
    print(letter)

# Using list in for loop
l =["alu", "mach", 98, "10 ta komola", 2.33, "lebu", 98969.23654589, 55, -120, "bazar krte hbe", 10]
for item in l:
    print(item)

# filter result
l2 = [25, 36, 21, 10, 35, 1, 2, 98, 5, 27, 21, 44, 11, 9, 17]
for i in l2:
    if i>=30:
        print(i)

# find 3 and 5 er divisible
for i in range(100):
    if i%3==0 and i%5==0:
        print(i)

# sum of numbers
sum = 0
for i in range(10):             # it is 0-9 ----- to get 1-10 = range(1,11)
    sum = sum+i
print(sum)