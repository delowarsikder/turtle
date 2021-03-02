import turtle as tl
import random
for i in range(60):
    tl.penup()
    tl.goto(random.randint(-300,300),random.randint(-300,300))
    tl.pendown()
    red_amount=random.randint(0,60)/100.0
    blue_amount=random.randint(50,100)/100.0
    green_amount=random.randint(0,70)/100.0
    tl.pencolor((red_amount,blue_amount,green_amount))
    circle_size=random.randint(10,40)
    tl.pensize(random.randint(1,5))
    tl.speed(10)
    for i in range(6):
        tl.circle(circle_size)
        tl.left(45)
tl.done()    
