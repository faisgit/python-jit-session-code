# for i in range(1,11):
#     print(i)

# take the number from the user and make the table of that number 

# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i }")

# use loop to iterate from 0 to 100 and print sum of all even number and print sum of odd number

# sum_of_even_num = 0
# sum_of_odd_num = 0

# for i in range(101):
#     if(i % 2 == 0):
#         sum_of_even_num = sum_of_even_num + i
#     else:
#         sum_of_odd_num = sum_of_odd_num + i

# print(f"The Sum of all even number is {sum_of_even_num} ")
# print(f"The Sum of all odd number is {sum_of_odd_num} ")


import math
a = 5.2
# print(math.trunc(a))
# print(math.floor(a))
# print(math.ceil(a))

# print("Helo" + 2)

print(3 + 4)
print("Hello" + "world ")

# print(4 + 2.6)
# 
# print(0.2 + 0.4 + 0.5)

import random

# print(random.random())
# print(random.randint(0,10))


# print("Hello world".lower())
# print("Hello world".upper())

# print(random.choice([1,2,3,4,5,56]))


a = "Good Morning"
# print(a[0])
# a[0] = "P"
# print(a)
# print(a[0:4])

# print(a[:4 ])

# print(a[-3:])

# print('  abc   ')
# print('  abc   '.strip())
a = "Good Morning"
# print(a.replace("Morning", "Night" ))
l = a.split(" ")
# print(l)
print(len(a))

#name = ['Faisal', "Harsh", "Tejas", "Sahil", 'piyush']
nums = [1, 2, 3, 4, 5]
# 
# print(nums[:3])
nums.append(51)
# print(nums)

# list methods
# pop methods, insert methods, remove methods.

print(5 in nums)


# Declare a list of your own and perform the operation like insert and remove element from the end of the list and add element in middle of list and remove middle element from the list  


# tuples
fruits = ("banana", 'orange', 'mango')

# length of tuples
# print(len(fruits))

# list to tuple

# print(list(fruits))

vegetables = ('Tomato', 'Potato', 'Onion')
print(fruits + vegetables)


# Sets 

# num = {1,2,3,5,1,3}
# num.add(34)
# # print(num[0])
# print(num)

# # Adding and Updating and deleting the sets

# # Joining two sets

# # num2 = {4,1,7,9}
# print(num.union(num2))

# print(list(num2))


# Convert the ages  to list and compare the len of the both sets and list and print which is bigger
dict = {
    "Name" : "Rahul",
    "age" : 23,
    "Birth_month" : "July"
}

# for key, values in dict.items():
#     print(f"{key} - {values}")

# print(dict["age"])

# dict['address']  = "Nagpur"
# print(dict)

# f  = open('open.txt', 'w')
# f.write("Hello world")
# f.close()
# 
# f = open('opens.txt', 'r') 
# text = f.read()
# print(text)
# f.close()

# import os
# os.remove('./open.txt')

def add():
    a =4
    b = 7
    return a + b
print(add())

def even_or_odd(num):
    if(num % 2 == 0):
        return f"{num} is even"
    else:
        return f"{num} is odd"
print(even_or_odd(4))