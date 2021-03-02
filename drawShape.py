# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 08:01:32 2020

@author: DelowaR
"""
import turtle as tl

running = True
tl.title('turtle GO')
screen = tl.getscreen()
tl.bgcolor(1, 1, 0)
# draw box using position
tl.goto(100, 0)
tl.goto(100, 50)
tl.goto(0, 50)
tl.home()  # move cursor into 0,0 position
# tl.backward(100)

tl.penup()
tl.goto(-100, -100)
tl.down()

# change the pen size
tl.pensize(10)

tl.circle(100)


# resize the turtle shape!
tl.shapesize(5, 5, 5)
tl.fillcolor('red')
tl.color('white', 'black')
tl.pencolor('green')

tl.up()
tl.goto(-150, -150)
tl.down()
# shift turtle
tl.forward(100)
tl.left(90)
tl.forward(100)
tl.right(90)
tl.forward(50)
tl.backward(100)

tl.dot(20)

tl.reset()
# change turtle
tl.shape('turtle')
# control turtle speed
tl.speed(2)
tl.forward(100)
tl.speed(10)
tl.right(90)
tl.forward(100)

tl.reset()

tl.pen(pencolor='red',fillcolor='green',pensize=5,speed=5)
tl.begin_fill()
tl.circle(100)
tl.end_fill()


tl.done()
