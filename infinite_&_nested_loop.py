# infinite loop
# We have to know that infinite loop is not available in for loop
# it only works in while loop.

a = 10
while a == 10:
    print(a)


while True:
    a = input("Enter a number: ")
    if a == "55" or a == "5":
        break
    print("Hello", a, "nice")


# when does a infinite loop work?
# it should always true and there should not be an increment or decrement.



# Nested loop 
for i in range (1, 6):
    for j in range (1, 6):
        print(i*j, end=" ")
    print()


a=1
while a<6:
    b=1
    while b<6:
        print(a*b, end=" ") 
        b=b+1 
    print()
    a=a+1