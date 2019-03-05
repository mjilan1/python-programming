#import turtle 

'''my_turtle = turtle.Turtle()

def square(length, angle):
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)

square(50, 90)
square(50, 90)
square(50, 90)
square(50, 90)'''

#I can make a sun 
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill ()
done ()
