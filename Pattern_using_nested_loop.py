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
