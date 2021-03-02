# https://blog.trinket.io/using-images-in-turtle-programs/
# some add here
import turtle as tl
import random
import sys
screen = tl.getscreen()
# screen.addshape('background.jpg')
screen.bgcolor('#000FA0')
# screen.bgpic('background.jpg')
# hidden inital turtle turtle
tl.title("Turtle race")
tl.hideturtle()

# set postion for both player
start_p1 = (-300, 100)
start_p2 = (-300, -100)
end_p1 = (300, 60)
end_p2 = (300, -140)
home_p1 = (260, 100)
home_p2 = (260, -100)
home_radius = 40

# create a player one
player_one = tl.Turtle()
player_one.shape('turtle')
player_one.color('red')
player_one.speed(1000)
player_one.penup()
player_one.goto(start_p1)
# create  a home as terminating point for player_one
player_one.goto(end_p1)
player_one.down()
player_one.circle(home_radius)
player_one.penup()
player_one.goto(start_p1)


# create a player two
player_two = tl.Turtle()
player_two.shape('turtle')
player_two.color('green')
player_two.speed(1000)
player_two.penup()
player_two.goto(-300, -100)

# create a home as terminating point for player_two
player_two.goto(end_p2)
player_two.down()
player_two.circle(home_radius)
player_two.penup()
player_two.goto(start_p2)

# creating a die list
die = [1, 2, 3, 4, 5, 6]

# control the game
player_one.speed(1)
player_two.speed(1)
running = True


def checkWin():
    if player_one.position() >= (home_p1):
        print('player_one is won the game')
        return 1
    elif player_two.pos() >= (home_p2):
        print('player_two is won the game')
        return 2


choice = int(input("Press 1 to turn player_one\nPress 2 to turn player_two\n"))
while(running):
    if checkWin() == 1:
        running = False
        # break;
    elif checkWin() == 2:
        running = False
        # break;
    else:
        # global choice
        # move forward player_one
        if choice == 1:
            player_one_trun = input("Press Enter to roll die for 1")
            p1_turn = random.choice(die)
            # print("The result of die turn p1 ",p1_turn)
            p1_step = p1_turn*10
            # print("The no of step p1",p1_step)
            player_one.forward(p1_step)
            if checkWin() == 1:
                break
            choice = 2
        # move forward player_two
        elif choice == 2:
            player_two_trun = input("Press Enter to roll die for 2")
            p2_turn = random.choice(die)
            # print("The result of die turn p2 ",p2_turn)
            p2_step = p2_turn*10
            # print("The no of step p1",p2_step)
            player_two.forward(p2_step)
            if checkWin() == 2:
                break
            choice = 1

print('END GAME')
screen.exitonclick()
sys.exit()
tl.done()
