# #
# ##
# ###
# ####
# #####
 
for i in range(5):
    for j in range(i+1):
        print("#", end="")
    print()



# 1
# 22
# 333
# 4444
# 55555

for i in range(5):
    for j in range(i+1):
        print(i, end="")
    print()


# 0
# 01
# 012
# 0123
# 01234

for i in range(5):
    for j in range(i+1):
        print(j, end="")
    print()



# a
# bb
# ccc
# dddd
# eeeee

for i in range(5):
    for j in range(i+1):
        print(chr(97+i), end="")
    print()



bazarer_List=[["Alu","Peyaj","Onno shobji"],[4,"hali kola", 2,"Kg peyara"],
              ["burger", 2.365, -32.62],["Misty", "laddu", 5, 3.550]]\
            
for bag in bazarer_List:
    for item in bag:
        print(item) 