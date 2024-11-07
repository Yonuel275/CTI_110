# yonuel vargas
# 11/7/2024
# P4LAB1
# Draw a square and triangle using turtle library

import turtle          
win = turtle.Screen()  
t = turtle.Turtle()
win.bgcolor("black")

t.pensize(4)            # increase pensize (takes integer)
t.pencolor("purple")     # set pencolor (takes string)
t.shape("turtle")

# While loop to draw a square
num = 0

while num < 4:
    t.forward(150)
    t.right(90)
    num += 1
print("while loop ends")

# For loop to draw a triangle

for tr in range(0,3):
    t.left(120)
    t.forward(200)
print("For loop has ended")
