import turtle as tl
screen=tl.getscreen()
'''
c=tl.clone()
c.color('blue')
tl.color('magenta')
tl.circle(20)
c.circle(50)'''

#draw a many circle
# tl.pen(pencolor='red',fillcolor='green')

tl.speed(100)
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for i in range(360):
    tl.pencolor(colors[i%6])
    tl.pensize(i/100+1)
    tl.forward(i)
    tl.left(91)


tl.done()