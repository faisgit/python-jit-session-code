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


# HomeWork Questions

#  1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer


# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age

# 3.Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

# Take the number from the user and find out whether the given number is prime or not 

num = int(input("Enter a number: "))
if(num < 0):
    print(f"{num} is not prime")
elif (num == 2 or num == 3 or num == 5 or num == 7 ):
    print(f"{num} is a prime number")
elif (num % 2 == 0 or num %3 ==0 or num % 5 == 0 or num % 7 == 0):
    print(f'{num} is not a prime number')
else:
    print(f"{num} is a prime number")