# Variables are declared here directly
# No data type is required
# Also no semicolon ; required finishing line

a = 10
b = "Nabil"
print (b, a)

# Input data is much easy, it finds data type by itself
a = input()                         # 10.236
b = input("Write name : ")          # Nabil
print("your input 1 is : " , a)        # your input 1 is :  10.236
print("your Name is : " , b)        # your Name is :  Nabil 

        ### Very IMPORTANT note ###
# Python takes all input as string
# Integer or float data also input as string


#------------------------------------------------------------------#

# Typecasting
# Converting data type from float to int / str to int or any other things

age = int(input())                  # 10
weight = float(input())             # 2.563
new_weight = int(weight)
print(type(age))                    # 10
print(type(weight))                 # 2.563
print(type(new_weight))             # 2