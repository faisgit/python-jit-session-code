# name = input("Enter your Name: ")
# print(name)
# num_one = int(input("Enter you first Number: "))
# num_two = int(input("Enter the Second Number: "))

# sum = num_one + num_two

# print(f'{num_one} + {num_two} = {sum}')


# # a = 10
# # b = '10'
# # c = int(b)
# # print(type(a) == type(c))

# import random

# print(random.random())

# Make '9.8' should be equal to 10
import math
x = '9.8'
convert_to_float = float(x)

# y = math.ceil(convert_to_float)
# print(y == 10)

# math.

num = 24
if(num % 2 == 0):
    print("It is an Even Number")
else:
    print("It is an odd Number")

# Write a Code which gives grade to students according to their grades
# 90-100 --> Grade A
# 70-89 --> Grade B
# 60-69 --> Grade C
# 50-59 --> Grade D 
# 0-49 --> Grade E
marks = 10
if(marks >= 90 and marks<=100):
    print("Grade A")
elif(marks >=70 and marks <=89):
    print("Grade B")
elif(marks >=60 and marks <=69):
    print("Grade C")
elif(marks >=50 and marks <=59):
    print("Grade D")
elif(marks >=40 and marks <=49):
    print("Grade E")
else:
    print("Grade F")


 