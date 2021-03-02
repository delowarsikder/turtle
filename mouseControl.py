import turtle as tl

def up():
    tl.stamp()
    tl.setheading(90)
    tl.forward(100)
def down():
    tl.stamp()
    tl.setheading(270)
    tl.forward(100)
def left():
    tl.stamp()
    tl.setheading(180)
    tl.forward(100)
def right():
    tl.stamp()
    tl.setheading(0)
    tl.forward(100)

def blue_screen():
    tl.bgcolor(0.0, 1.0, 0.0)

def white_screen():
    tl.bgcolor(1.0, 0.0, 0.0)

tl.listen()
tl.pensize(10)
tl.onkey(up,'Up')
tl.onkey(down,'Down')
tl.onkey(left,'Left')
tl.onkey(right,'Right')

tl.onkey(up, 'w')
tl.onkey(down, 's')
tl.onkey(left, 'a')
tl.onkey(right, 'd')

tl.onkeypress(blue_screen, 'space')
tl.onkey(white_screen, 'space')
tl.undo()

tl.done()