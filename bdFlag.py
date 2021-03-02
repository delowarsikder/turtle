##Draw Bangladeshi flag 
#process 1 static
import turtle as tl

# flag of bangladesh

tl.title('Bangladesh National Flag')
turtle_speed=5
tl.speed(turtle_speed)
#green box
tl.begin_fill()
tl.pen(pencolor='green',fillcolor='green')
tl.bgcolor('white')
tl.goto(200,0)
tl.goto(200,120)
tl.goto(0,120)
tl.home()
# tl.fillcolor('green')
tl.end_fill()
# red circle 
circle_radius=40
tl.up()
tl.goto(90,60)
tl.down()
tl.dot(80,'red')
#draw the stand 
tl.up()
tl.goto(0,125)
tl.down()
tl.pen(pencolor='#7F5217',pensize=10)
tl.right(90)
tl.forward(350)
# draw the base of flag
tl.pen(pensize=10,pencolor='#2B1B17',fillcolor='#2B1B17')
tl.begin_fill()
tl.right(90)
tl.forward(100)
tl.left(90)
tl.forward(50)
tl.left(90)
tl.forward(200)
tl.left(90)
tl.forward(50)
tl.left(90)
tl.forward(100)
tl.end_fill()
tl.hideturtle()
tl.reset()
# tl.done()

###process two more customize and dyanmic

tl.delay(100)

import turtle as tl
screen=tl.getscreen()
tl.title("Draw BD Flag")
#all color between 0 to 1
turtle_speed=1000
tl.speed(turtle_speed)
starting_point=tl.position()
bg_color='white'
tl.bgcolor((bg_color))
#height and width of flag 10:6
flag_width=300
flag_height=flag_width*.6
#radius of flag
radius=flag_width/5


def stop_draw(circle_center):
    x,y=circle_center
    global tl
    tl.penup()
    tl.goto(x,y)
    tl.pendown()


##draw the box of flag
box_color='green'
tl.pen(pencolor=box_color,fillcolor=box_color)
tl.begin_fill()
tl.forward(flag_width)
tl.left(90)
tl.forward(flag_height)
tl.left(90)
tl.forward(flag_width)
tl.left(90)
tl.forward(flag_height)
tl.left(90)
tl.end_fill()

#move cursor center
circle_color='#FF0000'
circle_center=(9*flag_width/20,flag_height/2)
stop_draw(circle_center)
#draw the circle with red color
tl.pen(pencolor=circle_color,fillcolor=circle_color)
tl.dot(radius*2,circle_color)

#draw stand
stand_color='#7F5217'
stand_height=450
stand_width=10
x,y=starting_point
top_left_corner=(x-stand_width/2,y+flag_height+10)
stop_draw(top_left_corner)
tl.pen(pencolor=stand_color,pensize=stand_width)
tl.right(90)
tl.forward(stand_height)

# draw the base of flag
tl.pen(pensize=10,pencolor='#2B1B17',fillcolor='#2B1B17')
tl.begin_fill()
tl.right(90)
tl.forward(100)
tl.left(90)
tl.forward(50)
tl.left(90)
tl.forward(200)
tl.left(90)
tl.forward(50)
tl.left(90)
tl.forward(100)
tl.end_fill()
tl.hideturtle()


tl.done()