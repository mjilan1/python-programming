#for a block of comments 
'''
no_of_students = 2
if no_of_students > 5:
    print ("This is a good class size")
else:
    print ("This is not a good class size")

    
grade = 79
if grade >= 80:
    print ("grade A")
if grade > 60 and grade <= 79:
    print ("grade B")
if grade >= 50 and grade < 60:
    print ("grade C")
'''
'''
Group class activity 
from random import *
x = randint (1,10)
user_input = input ("Enter your number")
val = int(user_input)

if x == val:
    print ("This is the right number")
else:
    print ("This is the wrong number")


def are_even(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("True")
        
    else: 
        print("False")

are_even(2, 4)

def light_ordark(hour):
    if hour > 24:
       print ("Thats not an hour in the day")
    elif hour >= 17 or hour < 7:
        print("Its dark outside")
    else:
        print("Its light outside")

light_ordark(20)'''

def sum_everything(*args):
    sum = 0
    for num in args:
        sum += num
    print(sum)

sum_everything(4, 5, 6)




