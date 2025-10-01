# Conditional Operations are if else statement basically -- works with bool value

# problem - 1 

rain = False
if rain == True:
    print("Ami school e jabo na")
else:
    print("Ami school e jabo")


# problem - 2

age = 17
if age >= 18:
    print("Tumi license paba")
else:
    print("Tumi 18-")



#------------------------------------------------------------------#

# Logical Operations are also works with bool value but it has also have some logical part

# and -- Both conditions must be True to return True
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# or -- If any one condition is True, result is True
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# not -- Reverses the value
# not True = False
# not False = True



# Problem - 3

marks = 85
if marks>=90 and marks <= 100:
    print("tumi duita candy box paba")
elif marks>=80 and marks <= 89:
    print("tumi ekta candy box paba")
else:
    print("tumi kichui paba na")
