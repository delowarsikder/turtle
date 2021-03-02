import turtle as tl
for angle in range(0,360,15):
    tl.setheading(angle)
    tl.forward(100)
    tl.write(str(angle)+'°')
    tl.penup()
    tl.backward(100)
    tl.pendown()

tl.penup()
tl.goto(150,150)
tl.pendown()


for i in range(100,-1,-1):
    tl.stamp()
    tl.left(i*15%15)
    tl.forward(20)

tl.done()    